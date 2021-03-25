<script lang="ts">
  import { item } from "./store.js";
  import Card, { Content, Actions } from "@smui/card";
  import Button, { Label } from "@smui/button";
  import Textfield, { Input, Textarea } from "@smui/textfield";
  import HelperText from "@smui/textfield/helper-text/index";
  import Select, { Option } from "@smui/select";

  let clicked: number = 0;

  let rooms = (async () => {
    const response = await fetch("./room", {
      method: "GET",
    });
    return response;
  })();
  console.log(rooms);
  function submit(): boolean {
    // Add a new item to the database.
    console.log(item);
    return true;
  }
</script>

<div class="card-container">
  <Card style="width: 320px;">
    <Content>
      <form>
        <Content>Add a new item</Content>
        <Textfield
          variant="outlined"
          bind:value={item.ItemName}
          label="Item name"
          input$aria-controls="helper-text-outlined-a"
          input$aria-describedby="helper-text-outlined-a"
        />
        <HelperText id="helper-text-outlined-a">Item name</HelperText>

        <!--<Select
          variant="outlined"
          bind:value={item.room}
          label="Fruit"
          anchor$class="demo-select-width"
          menu$class="demo-select-width"
        >
          <Option value="" />
          {#each rooms.HouseName as house}
            <Option value={house}>{house}</Option>
          {/each}
        </Select>-->
      </form>
    </Content>

    <Actions fullBleed>
      <Button on:click={submit}>
        <Label>Add item</Label>
        <i class="material-icons" aria-hidden="true">arrow_forward</i>
      </Button>
    </Actions>
  </Card>
</div>

<style lang="scss">
  .card-container {
    display: flex;
    justify-content: center;
  }
</style>
