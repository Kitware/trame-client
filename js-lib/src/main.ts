import { Trame } from "./trame";
import wslink from "./wslink";
import vtkURLExtract from "./URLExtract";

export default Trame;
export type { TrameConnectConfig } from "./trame";
export type { Decorator } from "./decorators";
export type { StateChangeEvent } from "./state";

export const { configDecorator, createClient } = wslink;
export const { extractURLParameters } = vtkURLExtract;
