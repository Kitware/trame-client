import vtk from "./vtk";
import fmt from "./fmt";

async function download(
  filename,
  contentOrPromise,
  type = "application/octet-stream"
) {
  const content = await Promise.resolve(contentOrPromise);
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.setAttribute("href", url);
  anchor.setAttribute("download", filename);
  document.body.appendChild(anchor);
  anchor.click();
  document.body.removeChild(anchor);
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function get(path, obj = window) {
  let current = obj;
  const exec = path.endsWith("()");
  const steps = (exec ? path.slice(0, -2) : path).split(".");
  for (let i = 0; i < steps.length; i++) {
    current = current[steps[i]];
  }
  if (exec) {
    return current();
  }
  return current;
}

function safe(obj) {
  try {
    JSON.stringify(obj);
    return obj;
  } catch (e) {
    // We need to look into object
  }

  const safeObj = {};
  const keys = Object.keys(obj);
  for (let i = 0; i < keys.length; i++) {
    const key = keys[i];
    const value = obj[key];
    if (Array.isArray(value)) {
      safeObj[key] = value.map(safe);
    } else {
      try {
        JSON.stringify(value);
        safeObj[key] = value;
      } catch (e) {
        continue;
      }
    }
  }
  return safeObj;
}

function toNode(id, key, value) {
  const node = { id };
  const prefix = key ? `${key}: ` : "";
  if (Array.isArray(value)) {
    node.name = `${prefix}[]`;
    if (value.length) {
      node.children = [];
    }
    return node;
  }
  if (value === null || !value) {
    node.name = `${prefix}${value}`;
    return node;
  }
  if (typeof value === "function") {
    node.name = `${prefix}function`;
    return node;
  }
  if (typeof value === "object") {
    node.name = `${prefix}{}`;
    if (Object.keys(value).length) {
      node.children = [];
    }
    return node;
  }
  node.name = `${prefix}${value}`;
  return node;
}

function registerItem(container, id, key, value) {
  const node = toNode(id, key, value);
  container.push(node);
  if (node.children) {
    registerList(id, node.children, value);
  }
}

function registerList(parentId, container, obj) {
  if (Array.isArray(obj)) {
    const key = null;
    for (let i = 0; i < obj.length; i++) {
      registerItem(container, `${parentId}_${i}`, key, obj[i]);
    }
  } else {
    const keys = Object.keys(obj);
    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];
      registerItem(container, `${parentId}_${i}`, key, obj[key]);
    }
  }
}

function tree(obj) {
  const result = [];
  registerList("", result, obj);
  return result;
}

export default {
  download,
  get,
  safe,
  tree,
  vtk,
  fmt,
};
