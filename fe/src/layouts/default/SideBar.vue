<template>
  <v-navigation-drawer permanent location="right">
    <!-- logo image -->
    <template v-slot:prepend>
      <div id="logo">
        <a @click="$router.push('/')">
          <img src="../../assets/logo.png" alt="logo" />
        </a>
      </div>
    </template>

    <v-divider class="mx-4"></v-divider>

    <!-- Home -->
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a
            @click="$router.push('/')"
            style="color: black; text-decoration: none"
          >
            <img src="../../assets/Home.png" alt="Home" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="mx-4"></v-divider>

    <!-- board menu -->
    <v-list v-model:opened="open" dense nav>
      <v-list-group>
        <template v-slot:activator="{ props }">
          <v-list-item v-bind="props" link class="menu-list">
            <v-list-item-content>
              <a
                @click="$router.push('/Board/Notice')"
                style="color: black; text-decoration: none"
              >
                <img src="../../assets/Board.png" alt="Board" />
              </a>
            </v-list-item-content>
          </v-list-item>
        </template>
        <!-- subMenu Board -->
        <v-list-item
          v-for="item in board"
          :key="item.name"
          :title="item.name"
          :value="item.name"
          @click="$router.push(item.href)"
        ></v-list-item>
      </v-list-group>
    </v-list>

    <v-divider class="mx-4"></v-divider>

    <!-- MyPage -->
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a
            @click="$router.push('/MyPage')"
            style="color: black; text-decoration: none"
          >
            <img src="../../assets/MyPage.png" alt="MyPage" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="mx-4"></v-divider>

    <!-- Setting -->
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a
            @click="$router.push('/Setting')"
            style="color: black; text-decoration: none"
          >
            <img src="../../assets/Setting.png" alt="Setting" />
          </a>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider class="mx-4"></v-divider>

    <!-- Logout -->
    <template v-slot:append> </template>
    <v-list dense nav>
      <v-list-item link class="menu-list">
        <v-list-item-content>
          <a
            @click="$router.push('/Setting')"
            style="color: black; text-decoration: none"
          >
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
    menu: [
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
