<template>
  <div>
    <TeamMatch />
  </div>
  <div class="Input User">
    <h1 class='text-pop-up-top'>Football 중계사이트 모음zip</h1>
    <div v-if="!loggedIn">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">ID:</label>
          <input type="text" id="name" v-model="id" />
        </div>
        <br>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" />
        </div>
        <br>
        <div>
          <label for="username">Gender:</label>
          <input type="text" id="gender" v-model="gender" />
        </div>
        <br>
        <div>
          <label for="password">Age:</label>
          <input type="text" id="age" v-model="age" />
        </div>
        <br>
        <button type="submit" class="custom-button">Log in</button>
      </form>
    </div>
    <div v-else>
      <h2>Welcome, {{ name }}!</h2>
      <button @click="logout" class="custom-button">Log out</button>
    </div>
    <div class="home">
      <h1>USER 생성</h1>
      <button @click="goToUserList" class="custom-button">Click</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

function goToUserList() {
  router.push({ name: 'CreateUser' }); // UserList 페이지로 이동
}

const id = ref('');
const password = ref('');
const gender = ref('');
const age = ref('');
const loggedIn = ref(false);
const name = ref('');

const login = () => {
  // 실제 로그인 로직은 여기에 구현되어야 합니다.
  // 로그인 성공 시 loggedIn 값을 true로 변경하고,
  // 사용자 이름을 name에 설정합니다.
  loggedIn.value = true;
  name.value = id.value; // 여기서는 임시로 ID를 이름으로 사용
};

const logout = () => {
  loggedIn.value = false;
  name.value = '';
  id.value = '';
  password.value = '';
  gender.value = '';
  age.value = '';
};
</script>

<style scoped>
.custom-button {
  padding: 15px 30px; /* 버튼 크기 조정 */
  font-size: 18px; /* 폰트 크기 조정 */
  background-color: #3498db; /* 버튼 배경색 */
  color: white; /* 버튼 텍스트 색상 */
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.custom-button:hover {
  background-color: #2980b9; /* 버튼 호버 시 배경색 변경 */
}
.text-pop-up-top {
	-webkit-animation: text-pop-up-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	        animation: text-pop-up-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}

 @-webkit-keyframes text-pop-up-top {
  0% {
    -webkit-transform: translateY(0);
            transform: translateY(0);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: none;
  }
  100% {
    -webkit-transform: translateY(-50px);
            transform: translateY(-50px);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: 0 1px 0 #cccccc, 0 2px 0 #cccccc, 0 3px 0 #cccccc, 0 4px 0 #cccccc, 0 5px 0 #cccccc, 0 6px 0 #cccccc, 0 7px 0 #cccccc, 0 8px 0 #cccccc, 0 9px 0 #cccccc, 0 50px 30px rgba(0, 0, 0, 0.3);
  }
}
@keyframes text-pop-up-top {
  0% {
    -webkit-transform: translateY(0);
            transform: translateY(0);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: none;
  }
  100% {
    -webkit-transform: translateY(-50px);
            transform: translateY(-50px);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: 0 1px 0 #cccccc, 0 2px 0 #cccccc, 0 3px 0 #cccccc, 0 4px 0 #cccccc, 0 5px 0 #cccccc, 0 6px 0 #cccccc, 0 7px 0 #cccccc, 0 8px 0 #cccccc, 0 9px 0 #cccccc, 0 50px 30px rgba(0, 0, 0, 0.3);
  }
}

</style>
