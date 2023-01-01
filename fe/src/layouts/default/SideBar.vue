<template>
  <v-navigation-drawer permanent location="right">
    <template v-slot:prepend>
      <!-- <v-list-item
        lines="two"
        prepend-avatar="https://randomuser.me/api/portraits/women/81.jpg"
        title="Jane Smith"
        subtitle="Logged in"
      ></v-list-item> -->
      <div id="logo">
        <a href="/">
          <img src="../../assets/logo.png" alt="logo" />
        </a>
      </div>
    </template>

    <v-divider class="mx-4"></v-divider>
    <v-spacer> </v-spacer>

    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a href="/" style="color: black; text-decoration: none">
            <img src="../../assets/Home.png" alt="Home" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-divider class="mx-4"></v-divider>

    <v-list v-model:opened="open" dense nav>
      <v-list-group>
        <template v-slot:activator="{ props }">
          <v-list-item v-bind="props" link class="menu-list">
            <v-list-item-content>
              <a
                href="/Board/Notice"
                style="color: black; text-decoration: none"
              >
                <img src="../../assets/Board.png" alt="Board" />
              </a>
            </v-list-item-content>
          </v-list-item>
        </template>
        <!-- <tr v-for="item in data" :key="item.num">
          <td>{{ item.num }}</td> -->
        <v-list-item
          v-for="item in board"
          :key="item.name"
          :title="item.name"
          :value="item.name"
          :href="item.href"
        ></v-list-item>
      </v-list-group>
    </v-list>

    <v-divider class="mx-4"></v-divider>
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a href="/MyPage" style="color: black; text-decoration: none">
            <img src="../../assets/MyPage.png" alt="MyPage" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-divider class="mx-4"></v-divider>
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a href="/Setting" style="color: black; text-decoration: none">
            <img src="../../assets/Setting.png" alt="Setting" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="mx-4"></v-divider>
    <template v-slot:append> </template>
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a href="/Setting" style="color: black; text-decoration: none">
            <img src="../../assets/Logout.png" alt="Logout" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data: () => ({
    open: [],
    items: [
      { href: "Home", img: "../../assets/Home.png" },
      { href: "Board", img: "../../assets/Board.png" },
      { href: "MyPage", img: "../../assets/MyPage.png" },
      { href: "Setting", img: "../../assets/Setting.png" },
    ],
    board: [
      { href: "/Board/Notice", name: "공지사항" },
      { href: "/Board/Academic", name: "학사공지" },
      { href: "/Board/Scholarship", name: "장학공지" },
      { href: "/Board/Job", name: "취업공지" },
    ],
  }),
};
</script>

<style scoped>
#logo img {
  width: 200px;
  height: auto;
}

#logo {
  text-align: center;
  margin-top: 30px;
  margin-bottom: 30px;
}

.menu-list img {
  height: 50px;
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
