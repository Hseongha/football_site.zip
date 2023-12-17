<template>
  
  <div class="container">
    
    <h1>모든 사용자 정보</h1>
    
    <button class="create-user-button" @click="createDialog열기">사용자 생성</button>
    <router-link to="/UserPrefer">
      <button class="user-prefer-button">모든 유저 선호팀</button>
    </router-link>
    <router-link to="/TeamMatch">
      <button class="team-match-button">진행 중인 경기</button>
    </router-link>
    <table class="user-table">
      <thead>
        <tr>
          <th>유저명</th>
          <th>성별</th>
          <th>나이</th>
          <th>동작</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.ID">
          <td>{{ user.NAME }}</td>
          <td>{{ user.GENDER }}</td>
          <td>{{ user.AGE }}</td>
          <td>
            <button @click="updateDialog열기(user)">업데이트</button>
            <button @click="사용자삭제(user)">삭제</button>
          </td>
        </tr>
      </tbody>
    </table>
    
     <!-- 업데이트 대화 상자 -->
  <div class="dialog-overlay" v-if="updateDialog표시">
    <div class="dialog update-dialog">
      <h2>사용자 정보 업데이트</h2>
      <form @submit.prevent="업데이트수행">
        <div class="form-group">
          <label for="name">이름:</label>
          <input v-model="업데이트데이터.name" required class="form-control">
        </div>
        <div class="form-group">
          <label for="gender">성별:</label>
          <input v-model="업데이트데이터.gender" required class="form-control">
        </div>
        <div class="form-group">
          <label for="age">나이:</label>
          <input v-model="업데이트데이터.age" required class="form-control">
        </div>
        <div class="form-group">
          <label for="password">비밀번호:</label>
          <input v-model="업데이트데이터.password" required class="form-control">
        </div>
        <div class="button-group">
          <button type="submit" class="btn btn-primary">업데이트</button>
          <button @click="updateDialog닫기" class="btn btn-secondary">취소</button>
        </div>
      </form>
      <p v-if="업데이트완료" class="success-message">업데이트가 완료되었습니다.</p>
    </div>
  </div>
    
    <!-- 사용자 생성 대화 상자 -->
    <div class="dialog-overlay" v-if="createDialog표시">
      <div class="dialog create-dialog">
        <h2>사용자 생성</h2>
        <form @submit.prevent="사용자생성">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="user.name" required>
          
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="user.password" required>
          
          <label for="gender">Gender:</label>
          <select id="gender" v-model="user.gender" required>
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
          
          <label for="age">Age:</label>
          <input type="number" id="age" v-model="user.age" required>
          
          <button type="submit">Create User</button>
          <button @click="createDialog닫기">취소</button>
        </form>
        <p v-if="create완료">사용자가 생성되었습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';


const isLoading = ref(true);
const users = ref([]);
const updateDialog표시 = ref(false);
const 업데이트데이터 = ref({
  name: '',
  gender: '',
  age: '',
  password: ''
});
let 선택된사용자 = null;
const 업데이트완료 = ref(false);
const user = ref({
  name: '',
  password: '',
  gender: 'male',
  age: 0
});
const createDialog표시 = ref(false);
const create완료 = ref(false);

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:5000/get_all_users');
    users.value = response.data;
  } catch (error) {
    console.error('모든 사용자 정보 불러오기 오류:', error);
  } finally {
    isLoading.value = false;
  }
});

const updateDialog열기 = (user) => {
  선택된사용자 = user;
  업데이트데이터.value = {
    name: user.NAME,
    gender: user.GENDER,
    age: user.AGE,
    password: ''
  };
  업데이트완료.value = false;
  updateDialog표시.value = true;
};

const 업데이트수행 = async () => {
  try {
    const response = await axios.put(`http://localhost:5000/update_user/${선택된사용자.ID}`, 업데이트데이터.value);
    console.log(`ID ${선택된사용자.ID}를 가진 사용자 업데이트 성공`, response.data);
    Object.assign(선택된사용자, 업데이트데이터.value);
     // 업데이트 완료 후, 모든 사용자 정보를 다시 가져와서 users에 할당
    const updatedUsers = await axios.get('http://localhost:5000/get_all_users');
    users.value = updatedUsers.data;

    업데이트완료.value = true;
    updateDialog닫기(); // 업데이트 완료 후 팝업 창 닫기
  } catch (error) {
    console.error(`ID ${선택된사용자.ID}를 가진 사용자 업데이트 오류:`, error);
  }
};

const updateDialog닫기 = () => {
  선택된사용자 = null;
  업데이트데이터.value = {
    name: '',
    gender: '',
    age: '',
    password: ''
  };
  updateDialog표시.value=false;
  업데이트완료.value = false;
};
const 사용자삭제 = async (user) => {
  try {
    const response = await axios.delete(`http://localhost:5000/delete_user/${user.ID}`);
    console.log(`ID ${user.ID}를 가진 사용자 삭제 성공`, response.data);
    users.value = users.value.filter(u => u.ID !== user.ID);
  } catch (error) {
    console.error(`ID ${user.ID}를 가진 사용자 삭제 오류:`, error);
  }
};
const createDialog열기 = () => {
  user.value = {
    name: '',
    password: '',
    gender: 'male',
    age: 0
  };
  createDialog표시.value = true;
};

const 사용자생성 = async () => {
  try {
    const response = await axios.post('http://localhost:5000/create_user', user.value);
    console.log('사용자 생성 성공', response.data);
    const updatedUsers = await axios.get('http://localhost:5000/get_all_users');
    users.value = updatedUsers.data;
    create완료.value = true;
    createDialog닫기();
  } catch (error) {
    console.error('사용자 생성 오류:', error);
  }
};

const createDialog닫기 = () => {
  user.value = {
    name: '',
    password: '',
    gender: 'male',
    age: 0
  };
  createDialog표시.value = false;
  create완료.value = false;
};
</script>


<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  position: relative; /* 부모 컨테이너에 position 설정 */
}

.user-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.user-table th,
.user-table td {
  padding: 10px;
  border: 1px solid #ccc;
  text-align: center;
}

.create-user-button {
  position: absolute;
  top:65px;
  left: 20px;
  bottom: 1010px;
  width: 150px; /* 버튼 가로 크기 고정 */
  height: 40px; /* 버튼 세로 크기 고정 */ /* 하단 여백 조정 */
}

.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.dialog {
  background: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.2);
}

.update-dialog {
  max-width: 400px;
  text-align: center;
}

.update-dialog form {
  margin: 0;
}

.form-group {
  margin-bottom: 15px;
}

.button-group {
  display: flex;
  justify-content: center;
  margin-top: 15px;
}

.button-group .btn {
  margin: 0 5px;
}

.success-message {
  color: green;
  margin-top: 10px;
}

.create-dialog {
  max-width: 400px;
}
.user-prefer-button {
  position: absolute;
  top:65px;
  bottom: 683px;
  right: 20px;
  width: 150px;
  height: 40px;
}
.team-match-button{
  position: absolute;
  top:20px;
  bottom: 100px;
  right: 20px;
  width: 150px;
  height: 40px;
}

/* 나머지 스타일링을 추가할 수 있습니다. */
</style>