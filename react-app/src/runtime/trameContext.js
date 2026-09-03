import { createContext, useContext } from "react";

export const TrameContext = createContext(null);

export function useTrame() {
  const ctx = useContext(TrameContext);
  if (!ctx) {
    throw new Error("useTrame() called outside of a <TrameContext.Provider>");
  }
  return ctx;
}
