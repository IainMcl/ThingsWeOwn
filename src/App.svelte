<script lang="ts">
  import ItemForm from "./ItemForm.svelte";
  import Modal from "./Modal.svelte";
  import Toasts from "./Toast.svelte";
  import { addToast } from "./toast_store";
  let logo = "build/static/logo.png";
</script>

<Modal>
  <div class="header">
    <img src={logo} alt="Things we own logo" />
  </div>
  <hr />
  <ItemForm />
</Modal>

<style lang="scss">
  .header {
    display: flex;
    justify-content: center;
    img {
      width: 10rem;
      max-height: 3rem;
    }
  }
</style>
