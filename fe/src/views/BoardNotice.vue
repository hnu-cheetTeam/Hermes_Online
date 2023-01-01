<template>
  <v-card class="contents" elevation="0">
    <SearchBar />
    <v-table class="table-contents">
      <thead>
        <tr>
          <th class="text-left">No.</th>
          <th class="text-left">제목</th>
          <th class="text-left">내용</th>
          <th class="text-left">일시</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data" :key="item.num">
          <td>{{ item.num }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.content }}</td>
          <td>{{ item.date }}</td>
        </tr>
      </tbody>
    </v-table>
  </v-card>
</template>

<script>
import SearchBar from "../components/SearchBar";
export default {
  name: "App",
  components: { SearchBar },
  data: () => ({
    data: [
      {
        num: 1,
        title: "[중앙도서관] 북챌린지 참여하여 독서장학금 받아요!",
        content:
          "겨울방학동안 독서토론 선정도서를 리마인드하고, 목표점수를 획득하면 독서장학금을...",
        date: "2022-12-30 16:03",
      },
      {
        num: 2,
        title: "[건강관리센터] 해외여행 건강정보 안내",
        content: "(이미지)",
        date: "2022-12-29 14:54",
      },
    ],
  }),
};
</script>

<style>
.contents {
  padding: 20px;
  margin: 20px;
}

.table-contents {
  padding: 10px;
}

th td {
  border-color: #daf5e0;
}
</style>
