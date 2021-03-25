<script lang="ts">
  import ItemForm from "./ItemForm.svelte";
  // let logo = "static/images/logo.png";
  let logo = "favicon.png";
  // const server = appenv.env.NGROK;
  // const fetchAll = async () => {
  // const response = await fetch(server + "/person");
  // return await response.json();
  // };

  // console.log(fetchAll());
</script>

<main>
  <div class="header">
    <img src={logo} alt="Things we own logo" />
  </div>
  <hr />
  <ItemForm />
</main>

<style lang="scss">
  .header {
    display: flex;
    justify-content: center;
    img {
      width: 10rem;
    }
  }
</style>
