<template>
  <RouterView />
</template>

<script>
export default {
  data: () => ({}),
};
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);
@font-face {
  font-family: "GmarketSansMedium";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "S-CoreDream-3Light";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

body {
  font-family: "S-CoreDream-3Light", "Noto Sans KR", sans-serif;
  background-color: #ced4f5;
  box-shadow: none;
}

.contents {
  padding: 5px;
  margin: 10px;
}
</style>
