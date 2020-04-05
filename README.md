# Snowdrop

Snowdrop is a simple echo service meant to demo the basic uses of gRPC.

## Protocol Buffers

In this directory, you'll find three important items.

1. `client` - contains all the client-side code.
2. `server` - contains all the server-side code.
3. `snowdrop.proto` - contains the API definitions.

It's also important to keep in mind that we are using two technologies here: Protocol Buffers and gRPC.

Protocol Buffers are ways of storing data compactly. While, gRPC uses these compact messages to send them over the web by using [RPCs](https://en.wikipedia.org/wiki/Remote_procedure_call).

## More Details

For more detailed explanations please see the `README.md`'s in the `client` and `server` directories as well as the files `server/main.go`, `client/main.py`, and `./snowdrop.proto`.

This tutorial will assume you have `go`, `python3`, and the following python submodules `virtualenv, pip`.