<template>
  <v-container style="padding: 10px">
    <h1>MY PAGE</h1>
    <div class="divider"></div>
    <v-row>
      <!-- User Avator -->
      <v-col class="setting-container">
        <v-row align="center" justify="start" style="margin: 20px">
          <v-avatar size="128" color="#DAF5E0">
            <!-- <v-img :src="userInfo.profileImg" alt="avatar"></v-img> -->
            <v-img src="../assets/logo.png" alt="avatar"></v-img>
          </v-avatar>
          <v-list-item-content style="margin-left: 20px">
            <v-list-item-title class="text-h4" style="margin-bottom: 10px">
              {{ userInfo.name }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ userInfo.nickName }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-row>
      </v-col>
      <!-- User Setting -->
      <v-col class="setting-container">
        <!-- Json Data
{
  profileImg: img         (프로필 사진)
  name: String              (이름)
  nickName: String       (닉네임)
  userId: String             (계정 아이디)
  userPw: String            (계정 패스워드)
  studentCode: int        (학번)
  birth: DATETIME         (생년월일)
  email: String               (이메일)
} -->
        <h2>Account</h2>
        <v-form ref="form" v-model="valid" lazy-validation>
          <!-- userName -->
          <v-text-field
            v-model="userInfo.name"
            :counter="10"
            :rules="nameRules"
            label="Name"
            required
          ></v-text-field>
          <!-- userNickName -->
          <v-text-field
            v-model="userInfo.nickName"
            :counter="10"
            :rules="nameRules"
            label="Nick Name"
            required
          ></v-text-field>
          <!-- userId -->
          <v-text-field
            v-model="userInfo.userId"
            :counter="10"
            :rules="nameRules"
            label="Account ID"
            required
          ></v-text-field>
          <!-- userPassword -->
          <v-text-field
            v-model="userInfo.userPw"
            :append-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="nameRules"
            :type="passwordShow ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            hint="At least 8 characters"
            counter
            @click:append="passwordShow = !passwordShow"
          ></v-text-field>

          <!-- userEmail -->
          <v-text-field
            v-model="userInfo.email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
          <!-- userStudentId -->
          <v-text-field
            v-model="userInfo.studentCode"
            :counter="10"
            :rules="nameRules"
            label="Student ID"
            required
          ></v-text-field>
          <!-- userBirth -->
        </v-form>

        <!-- <h2>Notifications</h2>
        <v-switch
          v-model="ex11"
          label="Account activity"
          color="success"
          value="success"
          hide-details
          inset
        ></v-switch>
        <v-switch
          v-model="ex11"
          label="News"
          color="success"
          value="success"
          hide-details
          inset
        ></v-switch>
        <v-switch
          v-model="ex11"
          label="Message"
          color="success"
          value="success"
          hide-details
          inset
        ></v-switch> -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    userInfo: {
      profileImg: "../assets/logo.png",
      name: "Hermes",
      nickName: "Hermes",
      userId: "hermes",
      userPw: "1234",
      studentCode: "20190700",
      birth: "2000-01-01",
      email: "test@hnu.kr",
    },
    valid: true,
    passwordShow: false,
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    passwordRules: [
      (v) => !!v || "Password is required.",
      (v) => v.length >= 8 || "Min 8 characters",
    ],
  }),
};
</script>

<style>
.setting-container {
  padding: 10px;
  margin: 10px;
  border: 5px solid #f5ebce;
  border-radius: 10px;
}
</style>
