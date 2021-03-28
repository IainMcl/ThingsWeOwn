<script lang="ts">
  import { item, house_room, person } from "./store.js";
  import Card, { Content, Actions } from "@smui/card";
  import Button, { Label } from "@smui/button";
  import Textfield, { Input, Textarea } from "@smui/textfield";
  // import IconButton, { Icon } from "@smui/icon-button";
  import HelperText from "@smui/textfield/helper-text/index";
  import Select, { Option } from "@smui/select";
  import FormField from "@smui/form-field";
  import Checkbox from "@smui/checkbox";

  import { getContext } from "svelte";
  // import { fly } from "svelte/transition";

  import HouseRoomPopup from "./HouseRoomPopup.svelte";
  import PersonPopup from "./PersonPopup.svelte";
  const { open } = getContext("simple-modal");

  let opening = false;
  let opened = false;
  let closing = false;
  let closed = false;

  const showHouseRoomPopup = (room_or_house: string, other: string): void => {
    open(HouseRoomPopup, { house_or_room: room_or_house, other: other });
  };

  const showPersonPopup = (): void => {
    open(PersonPopup);
  };

  let width = 95;

  let roomsPromise = getRooms();
  let housePromise = getHouses();
  let peoplePromise = getPeople();

  function getRooms() {
    return fetch("/available-rooms", { method: "GET" }).then((response) => {
      return response.json();
    });
  }

  function getHouses() {
    return fetch("/available-houses", { method: "GET" }).then((response) => {
      return response.json();
    });
  }

  function getPeople() {
    return fetch("/available-people", { method: "Get" }).then((response) => {
      return response.json();
    });
  }

  // const people = [{ Name: "Iain", Priority: 5 }];
  const sizes = ["Small", "Medium", "Large"];
  let options = [
    {
      name: "Fragile",
      disabled: false,
      value: $item.Fragile,
    },
    {
      name: "Keeping",
      disabled: false,
      value: $item.Keeping,
    },
    {
      name: "Owned",
      disabled: false,
      value: $item.Owned,
    },
    {
      name: "Moved",
      disabled: false,
      value: $item.Moved,
    },
  ];

  async function submit() {
    console.log("Submit");
    $item.Room = $item.House + " " + $item.Room;
    // $item.Owner = $person.name;
    const res = await fetch("/item", {
      method: "POST",
      body: JSON.stringify({
        ItemName: $item.ItemName,
        Room: $item.Room,
        Owner: $item.Owner,
        Value: $item.Value,
        Quantity: $item.Quantity,
        Size: $item.Size,
        Priority: $item.Priority,
        Fragile: $item.Fragile,
        Owned: $item.Owned,
        Moved: $item.Moved,
        Keeping: $item.Keeping,
        Notes: $item.Notes,
      }),
    });
    console.log(res.status);
    // const json = await res.json();
    // result = JSON.stringify(json);
  }
</script>

<div class="card-container">
  <Card style="width: {width}%;">
    <Content>
      <form on:submit|preventDefault>
        <Content>Add a new item</Content>
        <div class="item">
          <Textfield
            style="width: 100%;"
            variant="outlined"
            bind:value={$item.ItemName}
            label="Item name"
            input$aria-controls="helper-text-outlined-a"
            input$aria-describedby="helper-text-outlined-a"
          />
          <!-- <HelperText id="helper-text-outlined-a">Item name</HelperText> -->
        </div>

        <div class="group">
          <div class="item">
            <Select
              variant="outlined"
              bind:value={$item.House}
              label="House"
              anchor$class="demo-select-width"
              menu$class="demo-select-width"
            >
              <Option value="" />
              <!-- <Option>..loading..</Option> -->
              {#await housePromise}
                <Content>...loading...</Content>
              {:then houses}
                {#each houses as house}
                  <Option
                    style="text-transform: capitalize;"
                    value={house.HouseName}>{house.HouseName}</Option
                  >
                {/each}
              {:catch err}
                <code>{err.message}</code>
              {/await}
              <Option
                on:click={() => {
                  showHouseRoomPopup("House", $item.Room);
                }}>Add new house</Option
              >
            </Select>
            <!-- <HelperText-- id="helper-text-outlined-a" 
            >House and room information</HelperText-->
          </div>
          <div class="item">
            <Select
              variant="outlined"
              bind:value={$item.Room}
              label="Room"
              anchor$class="demo-select-width"
              menu$class="demo-select-width"
            >
              <Option value="" />
              {#await roomsPromise}
                <Content>...loading...</Content>
              {:then rooms}
                {#each rooms as room}
                  <Option style="text-transform: capitalize;" value={room.Room}
                    >{room.Room}</Option
                  >
                {/each}
              {:catch err}
                <code>{err.message}</code>
              {/await}
              <!-- {#each rooms as room}
                <Option value={room.Room}>{room.Room}</Option>
              {/each} -->
              <Option
                on:click={() => {
                  showHouseRoomPopup("Room", $item.House);
                }}
              >
                Add new room
                <!-- <IconButton class="material-icons">addoutlined</IconButton> -->
              </Option>
            </Select>
          </div>
        </div>
        <div class="item">
          <Select
            variant="outlined"
            bind:value={$item.Owner}
            label="Owner"
            anchor$class="demo-select-width"
            menu$class="demo-select-width"
          >
            <Option value="" />
            {#await peoplePromise}
              <Content>...loading...</Content>
            {:then people}
              {#each people as person}
                <Option style="text-transform: capitalize;" value={person.Name}
                  >{person.Name}</Option
                >
              {/each}
            {/await}
            <Option
              on:click={() => {
                showPersonPopup();
              }}
            >
              Add new person
              <!-- <IconButton class="material-icons">addoutlined</IconButton> -->
            </Option>
          </Select>
        </div>
        <div class="item">
          <Select
            variant="outlined"
            bind:value={$item.Size}
            label="Size"
            anchor$class="demo-select-width"
            menu$class="demo-select-width"
          >
            <Option value="" />
            {#each sizes as size}
              <Option value={size}>{size}</Option>
            {/each}
          </Select>
        </div>
        <div class="item">
          <Textfield
            style="width: 100%;"
            variant="outlined"
            bind:value={$item.Priority}
            label="Priority"
            type="number"
            input$aria-controls="helper-text-outlined-a"
            input$aria-describedby="helper-text-outlined-a"
          />
        </div>
        <div class="item grouped-check-boxes">
          {#each options as option}
            <FormField>
              <Checkbox
                bind:checked={option.value}
                value={option.name}
                disabled={option.disabled}
              />
              <span slot="label"
                >{option.name}{option.disabled ? " (disabled)" : ""}</span
              >
            </FormField>
          {/each}
        </div>
        <div class="margins">
          <Textfield
            fullwidth
            textarea
            bind:value={$item.Notes}
            label="Notes"
            input$aria-controls="helper-text-fullwidth-textarea"
            input$aria-describedby="helper-text-fullwidth-textarea"
          />
          <HelperText id="helper-text-fullwidth-textarea"
            >Any additional notes</HelperText
          >
        </div>
      </form>
    </Content>

    <Actions fullBleed>
      <Button on:click={submit}>
        <Label>Add item</Label>
        <i class="material-icons" aria-hidden="true">arrow_forward</i>
      </Button>
    </Actions>
  </Card>

  <div id="state">
    {#if opening}
      <p>opening modal...</p>
    {:else if opened}
      <p>opened modal!</p>
    {:else if closing}
      <p>closing modal...</p>
    {:else if closed}
      <p>closed modal!</p>
    {/if}
  </div>
</div>

<style lang="scss">
  // * :global(.demo-select_anchor) {
  //   width: 100%;
  // }

  * :global(select, .demo-select-width) {
    min-width: 200px;
    width: 100%;
    margin: auto;
  }
  .card-container {
    display: flex;
    // justify-content: center;
    padding-bottom: 1rem;
    justify-content: space-around;
  }
  .item {
    margin: 0.75rem;
  }
  .group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .grouped-check-boxes {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  // Fix text alignment within input fields to be centered.
  * :global(input) {
    margin: 0;
  }
</style>
