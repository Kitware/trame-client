async function loadEsModule(path) {
  try {
    return await import(path);
  } catch (e) {
    if (e instanceof TypeError) {
      // retry with forward slash
      return await import("/" + path);
    } else {
      throw e;
    }
  }
}

function lookupUmdModule(global_var_name) {
  const module = window[global_var_name];

  if (module) {
    return Promise.resolve(module);
  }

  const module_not_found_error = new ReferenceError(
    `UMD module not found at window.${global_var_name}`,
  );
  return Promise.reject(module_not_found_error);
}

function register_handle({ module, module_path }, function_name, handle_id) {
  const func = module[function_name];

  if (!func) {
    throw new ReferenceError(
      `Could not find function ${function_name} on module ${module_path}. Did you pass the correct function identifier?`,
    );
  }

  window.TRAME_EXTERNAL_SCRIPTS[handle_id] = {
    func,
  };
}

export async function registerUserScripts() {
  window.TRAME_EXTERNAL_SCRIPTS = {};
  const external_scripts =
    window.trame.state.state.trame__client_external_scripts || [];

  const module_registration_promises = [];

  for (const external_script of external_scripts) {
    console.debug("registering external_script ", external_script);

    const get_module_fn =
      external_script.module_type === "es" ? loadEsModule : lookupUmdModule;

    const registering_module = get_module_fn(external_script.path)
      .catch((e) => {
        throw new Error(
          `Could not load module ${external_script.path}. Did you pass the correct module path?`,
          {
            cause: e,
          },
        );
      })
      .then((module) => {
        register_handle(
          { module, module_path: external_script.path },
          external_script.function,
          external_script.id,
        );
      });

    module_registration_promises.push(registering_module);
  }

  const preload_results = await Promise.allSettled(
    module_registration_promises,
  );
  const failures = preload_results.filter(
    (result) => result.status === "rejected",
  );

  if (failures.length > 0) {
    const errors = failures.map((f) => f.reason);
    console.error(errors);
    throw new AggregateError(errors);
  }
}
