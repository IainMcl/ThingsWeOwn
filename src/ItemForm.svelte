<script lang="ts">
  import { item } from "./store.js";
  import Textfield, { Input, Textarea } from "@smui/textfield";
  import HelperText from "@smui/textfield/helper-text/index";
</script>

<h4>Add a new item</h4>
<form>
  <Textfield
    variant="outlined"
    bind:value={$item.ItemName}
    label="Item name"
    input$aria-controls="helper-text-outlined-a"
    input$aria-describedby="helper-text-outlined-a"
  />
  <HelperText id="helper-text-outlined-a">Item name</HelperText>
</form>

<style lang="scss">
  h4 {
    margin: 0;
  }
  form {
    width: 100%;
    margin: auto;
    .mdc-text-field {
      color: red;
    }
  }
  TextField {
    margin: auto;
  }
</style>
