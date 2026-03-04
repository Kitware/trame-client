export interface Decorator {
  priority: number;
  decorate(value: any): Promise<any>;
}

export const fileHandler: Decorator;
export const fileListHandler: Decorator;
export const fileInObjectHandler: Decorator;

export function registerDecorator(decorator: Decorator): void;
export function decorate(value: any): Promise<any>;
