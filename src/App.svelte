<script lang="ts">
  import ItemForm from "./ItemForm.svelte";
  //const dotenv = require("dotenv");
  let logo = "static/images/logo.png";
  const server = appenv.env.NGROK;
  const fetchAll = async () => {
    const response = await fetch(server + "/person");
    return await response.json();
  };

  console.log(fetchAll());
</script>

<main>
  <div class="header">
    <img src={logo} alt="Things we own logo" />
  </div>
  <ItemForm />
</main>

<style lang="scss">
  @media screen and (max-width: 640px) {
    main {
      img {
        width: 10rem;
      }
    }
  }
</style>
