<script lang="ts">
  import { Content, Actions } from "@smui/card";
  import Textfield from "@smui/textfield";
  import Button, { Label } from "@smui/button";

  import { person } from "./store.js";

  async function addPerson() {
    const res = await fetch("/person", {
      method: "POST",
      body: JSON.stringify({
        Name: $person.name,
        Priority: $person.priority,
      }),
    });
    console.log(res.status);
    // const json = await res.json();
    // result = JSON.stringify(json);
  }
</script>

<form on:submit|preventDefault>
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
    <Button on:click={addPerson}>
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
