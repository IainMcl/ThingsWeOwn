import { writable } from 'svelte/store';

export const item = writable({
  ItemName: "",//
  House: "",//
  Room: "",//
  Owner: "",//
  Value: 0,
  Quantity: 1,
  Size: "small",//
  Priority: 1,//
  Fragile: false,//
  Owned: true,//
  Moved: false,//
  Keeping: true,//
  Notes: ""
})

export const house_room = writable({
  house: "",
  room: ""
})

export const person = writable({
  name: "",
  priority: 1
})