## Trame client library for plain JS

This library aims to simplify integration of any web client with a trame server.

## Examples

- [CDN](./examples/cdn/)
- [Vite](./examples/vite/)

## Usage

```js
const trame = new Trame()
await trame.connect({ application: 'trame' });

// State handing
trame.state.set("a", 5);
console.log(trame.state.get("b"));
trame.state.update({
    a: 1,
    b: 2,
});
trame.state.watch(["a"], (a) => {
    console.log(`a changed to ${a}`);
})

// Method call on Python
const result = await trame.trigger("name", [arg_0, arg_1], { kwarg_0: 1, kwarg_1: 2 });

// Register JS object so Python can make method calls
// py => server.js_call("name", "method", arg_0, arg_1) 
trame.refs["name", js_object];
```

More API examples 

```js

// Connect to server and wait until connected
// - sessionURL
// - sessionManagerURL
await trame.connect({ application: "trame" });

// custom serializer registration for method/state
trame.registerDecorator()

// same as waiting on connect
await trame.ready

// Listen to connection status change
const unsubscribeOnClose = trame.onClose((info) => {
    console.log("connection closed", info);
});
unsubscribeOnClose();

// Listen to connection status change
const unsubscribeOnError = trame.onError((info) => {
    console.log("connection error", info);
});
unsubscribeOnError();

// Listen to connection status change
const unsubscribeOnDisconnect = trame.onDisconnect(() => {
    console.log("Client is disconnecting");
});
unsubscribeOnDisconnect();

// Ask server to exit and disconnect
trame.exit(timeout);

// Disconnect from server but don't ask the server to exit
trame.disconnect();

// Try to reconnect using the same info as before after a onClose
await trame.reconnect();

// -----------------------------------
// WsClient API
// -----------------------------------
console.log(trame.client);

// -----------------------------------
// State API
// -----------------------------------
console.log(trame.state);

// set
trame.state.set("a", 2);
trame.state.set('b', 3);
trame.state.update({
    a: 2.5,
    b: 3.5,
    c: 4.5,
})

// get
console.log(trame.state.get("c"));
console.log(trame.state.get('a'));

// force send to server
trame.state.flush('a', 'b');

// listener for state change
const unsubscribe = trame.state.onChange(({ type, keys }) => {
    if (type === "dirty-state") {
        console.log(`${keys} have changed`);
    } else if (type === "new-keys") {    
        console.log(`${keys} have been added`);
    } else {
        console.log(`Unkown type(${type}) of message`)
    }
});
unsubscribe();

// simpler api for state change
const unsubscribe2 = trame.state.watch(
    ["a", "b", "c"], 
    (a, b, c) => {
        console.log(`a(${a}) or b(${b}) or c(${c}) have changed`);
    }
);
unsubscribe2();

// -----------------------------------
// Method execution API
// -----------------------------------

// method execution on Python side
trame.trigger("name", ['arg_0', 'arg_1'], { kwarg_0: 1,  kwarg_1: 2 });

// object registration on JS side so Python can execute methods on them
trame.refs["ref_name"] = console;
```
