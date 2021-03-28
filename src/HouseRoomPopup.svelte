<script lang="ts">
  import { Content, Actions } from "@smui/card";
  import Textfield from "@smui/textfield";
  import Button, { Label } from "@smui/button";
  import { house_room } from "./store.js";

  export let house_or_room: string;
  export let other: string;

  // let value;
  // let other_value;

  let value = house_or_room === "House" ? $house_room.house : $house_room.room;
  let other_value =
    house_or_room === "House" ? $house_room.room : $house_room.house;

  let other_item: string;
  if (other === "undefined" || other === "") {
    other_item = house_or_room === "House" ? "Room" : "House";
  }

  async function addHouseRoom() {
    if (other === "undefuned" || other === "") {
      if (house_or_room === "House") {
        $house_room.house = value;
        $house_room.room = other_value;
      } else {
        $house_room.room = value;
        $house_room.house = other_value;
      }
    } else {
      if (house_or_room === "Room") {
        $house_room.house = other;
        $house_room.room = value;
      } else if (house_or_room === "House") {
        $house_room.room = other;
        $house_room.house = value;
      }
    }
    console.log($house_room);
    const res = await fetch("/room", {
      method: "POST",
      body: JSON.stringify({
        House: $house_room.house,
        Room: $house_room.room,
      }),
    });
    console.log(res.status);
    // const json = await res.json();
    // result = JSON.stringify(json);
  }
</script>

<form>
  <Content>
    {#if other === "undefined" || other === ""}
      Add a new House and Room
    {:else if house_or_room === "Room"}
      Add a new Room to '{other}'
    {:else}
      Add a new House with '{other}'
    {/if}
  </Content>
  <div class="item">
    <Textfield
      style="width: 100%;"
      variant="outlined"
      bind:value
      label={house_or_room}
      input$aria-controls="helper-text-outlined-a"
      input$aria-describedby="helper-text-outlined-a"
    />
  </div>

  {#if other === "undefined" || other === ""}
    <div class="item">
      <Textfield
        style="width: 100%;"
        variant="outlined"
        bind:value={other_value}
        label={other_item}
        input$aria-controls="helper-text-outlined-a"
        input$aria-describedby="helper-text-outlined-a"
      />
    </div>
  {/if}
  <Actions fullBleed>
    <Button on:click={addHouseRoom}>
      <Label>Add item</Label>
      <i class="material-icons" aria-hidden="true">arrow_forward</i>
    </Button>
  </Actions>
</form>

<style>
  * :global(input) {
    margin: 0;
  }

  .item {
    margin: 0.5rem;
  }

  /* h2 {
    font-size: 2rem;
    text-align: center;
  } */
</style>
