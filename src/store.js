import { writable } from 'svelte/store';

export const item = writable({
  ItemName: "",
  House: "",
  Room: ""
})