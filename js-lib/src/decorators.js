function compareDecorator(a, b) {
  return a.priority - b.priority;
}

export const fileHandler = {
  priority: 0,
  async decorate(value) {
    if (value === null || value === undefined) return value;
    if (value.constructor && value.constructor === File) {
      const { name, lastModified, size, type } = value;
      const arrayBuffer = await new Promise((resolve) => {
        const reader = new FileReader();
        reader.addEventListener("loadend", () => {
          resolve(reader.result);
        });
        reader.readAsArrayBuffer(value);
      });
      const content = new DataView(arrayBuffer);
      return {
        name,
        lastModified,
        size,
        type,
        content,
        // used by server to prevent sending those fields back to JS
        _filter: ["content"],
      };
    }
    return value;
  },
};

export const fileListHandler = {
  priority: 0,
  async decorate(value) {
    if (value === null || value === undefined) return value;
    if (typeof value === "string") {
      return value;
    }
    if ((value.constructor && value.constructor === FileList) || value.length) {
      const results = [];
      /* eslint-disable no-await-in-loop */
      for (let i = 0; i < value.length; i++) {
        results.push(await fileHandler.decorate(value[i]));
      }
      /* eslint-enable no-await-in-loop */
      return results;
    }
    return value;
  },
};

export const fileInObjectHandler = {
  priority: 0,
  async decorate(value) {
    if (value === null || value === undefined) return value;
    if (typeof value === "string") {
      return value;
    }
    if (value.constructor && value.constructor === Object) {
      const newValue = {};
      const names = Object.keys(value);
      /* eslint-disable no-await-in-loop */
      for (let i = 0; i < names.length; i++) {
        const name = names[i];
        newValue[name] = value[name];
        newValue[name] = await fileListHandler.decorate(newValue[name]);
        newValue[name] = await fileHandler.decorate(newValue[name]);
      }
      /* eslint-enable no-await-in-loop */
      return newValue;
    }
    return value;
  },
};

// ----------------------------------------------------------------------------
// API
// ----------------------------------------------------------------------------

const STATE_DECORATORS = [fileHandler, fileListHandler, fileInObjectHandler];

export function registerDecorator(decorator) {
  STATE_DECORATORS.push(decorator);
  STATE_DECORATORS.sort(compareDecorator);
}

export async function decorate(value) {
  let result = value;
  /* eslint-disable no-await-in-loop */
  for (let i = 0; i < STATE_DECORATORS.length; i++) {
    if (result === null || result === undefined) {
      return result;
    }
    result = await STATE_DECORATORS[i].decorate(result);
  }
  /* eslint-enable no-await-in-loop */
  return result;
}
