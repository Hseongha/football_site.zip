<!--<template>
    <div>
      <h1>사용자 정보 업데이트</h1>
      <form @submit.prevent="updateUserInfo">
        <div>
          <label for="name">이름:</label>
          <input type="text" id="name" v-model="userData.name" />
        </div>
        <div>
          <label for="password">비밀번호:</label>
          <input type="password" id="password" v-model="userData.password" />
        </div>
        <div>
          <label for="gender">성별:</label>
          <input type="text" id="gender" v-model="userData.gender" />
        </div>
        <div>
          <label for="age">나이:</label>
          <input type="text" id="age" v-model="userData.age" />
        </div>
        <button type="submit">정보 업데이트</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios';
  
  const router = useRouter();
  const userId = ref(0); // 사용자 ID
  const userData = ref({
    name: '',
    password: '',
    gender: '',
    age: ''
  });
  
  onMounted(() => {
    // 현재 페이지의 route 파라미터에서 사용자 ID를 가져옵니다.
    userId.value = router.currentRoute.value.params.id;
  
    // 사용자 정보를 가져와서 userData에 설정합니다.
    fetchUserInfo(userId.value);
  });
  
  const fetchUserInfo = async (id) => {
    try {
      const response = await axios.get(`http://192.168.0.24:5000/get_user/${id}`);
      const user = response.data;
      userData.value = {
        name: user.NAME,
        password: user.PASSWORD,
        gender: user.GENDER,
        age: user.AGE
      };
    } catch (error) {
      console.error('Error fetching user info:', error);
    }
  };
  
  const updateUserInfo = async () => {
    try {
      const response = await axios.put(`http://192.168.0.24:5000/update_user/${userId.value}`, userData.value);
      console.log('User info updated successfully', response.data);
      router.push('/GetAllUsers'); // 업데이트 후 목록 페이지로 이동
    } catch (error) {
      console.error('Error updating user info:', error);
    }
  };
  </script>
  
  <style scoped>
  /* 스타일링을 추가할 수 있습니다. */
  </style>
-->
  