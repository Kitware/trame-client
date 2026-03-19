const load_module = async function load_module(path) {
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
};

const register_preprocessor = async function register_preprocessor(module_path, function_name, preprocessor_id) {
    let module;
    try {
        module = await load_module(module_path);
    } catch (e) {
        throw new Error(`Could not load module ${module_path}. Did you pass the correct module path?`, {
            cause: e
        });
    }
    const func = module[function_name];

    if (!func) {
        throw new ReferenceError(`Could not find function ${function_name} on module ${module_path}. Did you pass the correct function identifier?`)
    }

    window.TRAME_CLIENT_PREPROCESSING[preprocessor_id] = {
        preprocess: func
    }
}

export async function registerPreprocessingLogic() {
    window.TRAME_CLIENT_PREPROCESSING = {}
    const preprocessors = window.trame.state.state.trame__client_preprocessing;

    const promises = [];

    for (const preprocessor of preprocessors) {
        console.debug("registering preprocessor ", preprocessor);
        promises.push(
            register_preprocessor(preprocessor.path, preprocessor.function, preprocessor.id)
        );
    }

    const preload_results = await Promise.allSettled(promises);
    const failures = preload_results.filter(result => result.status === 'rejected');

    if (failures.length > 0) {
        const errors = failures.map(f => f.reason);
        console.error(errors);
        throw new AggregateError(errors);
    }
}
