export interface Decorator {
  priority: number;
  decorate(value: any): Promise<any>;
}

function compareDecorator(a: Decorator, b: Decorator): number {
  return a.priority - b.priority;
}

export const fileHandler: Decorator = {
  priority: 0,
  async decorate(value: any): Promise<any> {
    if (value === null || value === undefined) return value;
    if (value.constructor && value.constructor === File) {
      const { name, lastModified, size, type } = value as File;

      // Will be null in the event of an error on read, DataView otherwise
      let content: DataView | null = null;
      // Will be an error string if content failed to read, null otherwise
      let error: string | null = null;

      try {
        const arrayBuffer = await new Promise<ArrayBuffer>(
          (resolve, reject) => {
            const reader = new FileReader();
            reader.addEventListener("loadend", () => {
              resolve(reader.result as ArrayBuffer);
            });
            reader.addEventListener("error", () => {
              reject(reader.error);
            });
            reader.readAsArrayBuffer(value);
          },
        );

        content = new DataView(arrayBuffer);
      } catch (e: any) {
        error = e?.message ?? String(e);
      }

      return {
        name,
        lastModified,
        size,
        type,
        content,
        error,
        // used by server to prevent sending those fields back to JS
        _filter: ["content"],
      };
    }
    return value;
  },
};

export const fileListHandler: Decorator = {
  priority: 0,
  async decorate(value: any): Promise<any> {
    if (value === null || value === undefined) return value;
    if (typeof value === "string") {
      return value;
    }
    if ((value.constructor && value.constructor === FileList) || value.length) {
      const results = await Promise.allSettled(
        Array.from(value as ArrayLike<File>).map((file) =>
          fileHandler.decorate(file),
        ),
      );
      return results.map((result: any) => result.value);
    }
    return value;
  },
};

export const fileInObjectHandler: Decorator = {
  priority: 0,
  async decorate(value: any): Promise<any> {
    if (value === null || value === undefined) return value;
    if (typeof value === "string") {
      return value;
    }
    if (value.constructor && value.constructor === Object) {
      const newValue: Record<string, any> = {};
      const names = Object.keys(value);

      for (let i = 0; i < names.length; i++) {
        const name = names[i];
        newValue[name] = value[name];
        newValue[name] = await fileListHandler.decorate(newValue[name]);
        newValue[name] = await fileHandler.decorate(newValue[name]);
      }

      return newValue;
    }
    return value;
  },
};

// ----------------------------------------------------------------------------
// API
// ----------------------------------------------------------------------------

const STATE_DECORATORS: Decorator[] = [
  fileHandler,
  fileListHandler,
  fileInObjectHandler,
];

export function registerDecorator(decorator: Decorator): void {
  STATE_DECORATORS.push(decorator);
  STATE_DECORATORS.sort(compareDecorator);
}

export async function decorate(value: any): Promise<any> {
  let result = value;

  for (let i = 0; i < STATE_DECORATORS.length; i++) {
    if (result === null || result === undefined) {
      return result;
    }
    result = await STATE_DECORATORS[i].decorate(result);
  }

  return result;
}
