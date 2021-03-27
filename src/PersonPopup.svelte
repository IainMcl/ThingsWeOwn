<script lang="ts">
  import { Content, Actions } from "@smui/card";
  import Textfield from "@smui/textfield";
  import Button, { Label } from "@smui/button";

  import { person } from "./store.js";

  const submit = () => {
    console.log("submit");
  };
</script>

<form>
  <Content>Add a new person</Content>
  <div class="item">
    <Textfield
      style="width: 100%;"
      variant="outlined"
      bind:value={$person.name}
      label="Name"
      input$aria-controls="helper-text-outlined-a"
      input$aria-describedby="helper-text-outlined-a"
    />
  </div>
  <div class="item">
    <Textfield
      style="width: 100%;"
      variant="outlined"
      bind:value={$person.priority}
      label="Priority"
      type="number"
      input$aria-controls="helper-text-outlined-a"
      input$aria-describedby="helper-text-outlined-a"
    />
  </div>

  <Actions fullBleed>
    <Button on:click={submit}>
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

  h2 {
    font-size: 2rem;
    text-align: center;
  }
</style>
