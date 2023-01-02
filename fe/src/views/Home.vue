<template>
  <v-card class="contents" elevation="0">
    <SearchBar />
    <v-row>
      <v-col>
        <h1>실시간 게시글</h1>
        <v-sheet class="mx-auto">
          <v-slide-group
            v-model="model"
            class="pa-4"
            selected-class="bg-success"
            show-arrows
          >
            <v-slide-group-item v-for="item in realtimePost" :key="item">
              <v-card
                class="ma-4 out-container"
                height="320"
                width="280"
                elevation="0"
              >
                <div class="inner-container">
                  <div class="realtime-post-content">
                    <p
                      style="
                        font-size: 15px;
                        color: #999999;
                        margin-bottom: 10px;
                      "
                    >
                      {{ item.class }}
                    </p>
                    <p
                      style="
                        font-size: 20px;
                        font-weight: 600;
                        margin-bottom: 10px;
                      "
                    >
                      {{ item.title }}
                    </p>
                    <p style="margin-bottom: 10px">{{ item.dateCreated }}</p>
                    <div
                      class="is-file"
                      v-show="item.isFile"
                      style="margin-bottom: 10px"
                    >
                      <p>파일 아이콘 자리</p>
                    </div>
                  </div>
                </div>
              </v-card>
            </v-slide-group-item>
          </v-slide-group>
        </v-sheet>
      </v-col>
    </v-row>

    <v-row>
      <div class="divider"></div>
    </v-row>

    <v-row>
      <v-col>
        <h1>최근 본 게시글</h1>
        <br />
        <v-table class="out-container rounded-lg">
          <thead class="inner-container">
            <tr>
              <th class="text-left">분류</th>
              <th class="text-left">No.</th>
              <th class="text-left">제목</th>
              <th class="text-left">게시일</th>
            </tr>
          </thead>
          <tbody style="background-color: #fdfbf5">
            <tr v-for="item in recentPost" :key="item.postNum">
              <td>{{ item.class }}</td>
              <td>{{ item.postNum }}</td>
              <td>{{ item.title }}</td>
              <td>{{ item.dateCreated }}</td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import api from "@/api";
import SearchBar from "../components/SearchBar";
export default {
  name: "App",
  components: { SearchBar },
  data: () => ({
    model: null,
    realtimePost: [
      {
        class: "공지게시판",
        dateCreated: "2022-12-30 16:03",
        title: "[중앙도서관] 북챌린지 참여하여 독서장학금 받아요!",
        isFile: true,
      },
    ],
    recentPost: [
      {
        class: "공지게시판",
        postNum: 1,
        title: "[중앙도서관] 북챌린지 참여하여 독서장학금 받아요!",
        dateCreated: "2022-12-30 16:03",
      },
    ],
  }),
  created() {
    // 실시간 게시글
    api.get("/main/realtimepost").then((res) => {
      this.realtimePost = res.data;
    });
    // 최근 본 게시글
    api.get("/main/recentpost").then((res) => {
      this.recentPost = res.data;
    });
  },
};
</script>

<style>
.out-container {
  background-color: #fdfbf5;
  /* outline: none; */
  box-shadow: 5px 5px #f4eacf;
  border: #f5ead0 3px solid;
  /* outline-offset: 3px; */
  border-radius: 10px;
}

.inner-container {
  border: #ffffff 3px solid;
  border-radius: 10px;
  background-color: #fdfbf5;
  height: 100%;
}

.realtime-post-content {
  margin: 20px;
}

.recent-post-container {
  background-color: #fdfbf5;
  /* outline: none; */
  /* box-shadow: 5px 5px #f5ead0; */
  border: #f5ead0 5px solid;
  outline-offset: 3px;
  border-radius: 10px;
}

.divider {
  border: #fee580 2px solid;
  margin-top: 10px;
  margin-right: auto;
  margin-left: auto;
  margin-bottom: 30px;
  width: 95%;
  height: 2px;
}

.contents {
  padding: 20px;
  margin: 20px;
}
</style>
