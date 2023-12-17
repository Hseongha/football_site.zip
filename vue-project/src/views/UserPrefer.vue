<template>
    <div>
      <h1>유저 선호 팀</h1>
      <p v-if="isLoading">Loading...</p>
      
      <table v-else class="table">
        <thead>
          <tr>
            <th>유저명</th>
            <th>나이</th>
            <th>성별</th>
            <th>선호 팀</th>
            <th>팀 엠블럼</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="prefer in userPreferences" :key="prefer['ID']">
            <td>{{ prefer["USER_NAME"] }}</td>
            <td>{{ prefer["AGE"] }}</td>
            <td>{{ prefer["GENDER"] }}</td>
            <td>{{ prefer["PREFER_TEAM"] }}</td>
            <td>
              <img
                :src="getImageSrc(prefer['TEAM_EMBLEM'])"
                alt="Team Emblem"
                class="team-emblem"
              />
            </td>
          </tr>
        </tbody>
      </table>
      <router-link to="/TeamMatch">현재 진행 중인 경기</router-link><br><br><br>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const isLoading = ref(true);
  const userPreferences = ref([]);
  
  const getImageSrc = (emblemPath) => `http://localhost:5000/static/${emblemPath}`;
  
  onMounted(async () => {
    try {
      const response = await axios.get('http://localhost:5000/get_user_prefer');
      userPreferences.value = response.data;
    } catch (error) {
      console.error('Error fetching user preferences:', error);
    } finally {
      isLoading.value = false;
    }
  });
  </script>
  
  <style scoped>
  .team-emblem {
    max-width: 120px;
    max-height: 120px;
  }
  </style>
  