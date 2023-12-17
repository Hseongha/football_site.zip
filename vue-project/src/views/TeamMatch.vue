<template>
  <div class="team vs team">
    <h1>경기 정보</h1>
    <template v-if="isLoading">
      <p>Loading...</p>
    </template>
    <template v-else>
      <div class="table-container">
        <table class="table">
          <thead>
            <tr>
              <th>홈팀</th>
              <th>&nbsp;</th>
              <th>어웨이팀</th>
              <th>&nbsp;</th>
              <th>경기 날짜</th>
              <th>경기 시간</th>
              <th>중계사이트</th>
              <th>사이트link</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="match in matches" :key="match['ID']">
              <td>{{ match["HOME_TEAM_NAME"] }}</td>
              <td>
                <img
                  :src="getImageSrc(match['HOME_TEAM_EMBLEM'])"
                  alt="Team Emblem"
                  class="team-emblem"
                />
              </td>
              <td>{{ match["AWAY_TEAM_NAME"] }}</td>
              <td>
                <img
                  :src="getImageSrc(match['AWAY_TEAM_EMBLEM'])"
                  alt="Team Emblem"
                  class="team-emblem"
                />
              </td>
              <td>{{ match["DATES"] }}</td>
              <td>{{ match["TIMES"] }}</td>
              <td>{{ match["CONNECTED_SITE"] }}</td>
              <td class="table-cell">
                <button class="site-button" @click="goToSite(match['CONNECTED_SITE_LINK'])">
                  {{ match["CONNECTED_SITE"] }}
                </button>
                </td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      isLoading: true,
      matches: [],
    };
  },
  methods: {
    getImageSrc(emblemPath) {
      return `http://localhost:5000/static/${emblemPath}`;
    },
    async goToSite(link) {
      if (link) {
        window.open(link, "_blank");
      }
    },
  },
  async mounted() {
    try {
      const response = await axios.get("http://localhost:5000/get_team_match");
      
      this.matches = response.data;
      const responseConnected = await axios.get("http://localhost:5000/get_match_site");
      this.matches.forEach((match, index) => {
        match.CONNECTED_SITE = responseConnected.data[index].CONNECTED_SITE;
        match.CONNECTED_SITE_LINK = responseConnected.data[index].CONNECTED_SITE_LINK;
      });
      


    } catch (error) {
      console.error("Error fetching team match data:", error);
    } finally {
      this.isLoading = false;
    }
  },
};
</script>

<style scoped>
.team-emblem {
  max-width: 120px;
  max-height: 120px;
}

.table-container {
  width: 100%;
  overflow-x: auto;
  text-align:center;
}
.table {
  margin: 0 auto; /* 테이블 가운데 정렬 */
  width: 100%;
  border-collapse:collapse;
}
.table-cell {
  padding : 10px;
  font-size:13px;
  font-family :Arial, sans-serif;
  border:1px solid #ccc;
}
.site-button {
  background-color: #bf34db;
  color: #4c1941;
  border: none;
  padding: 30px 10px;
  border-radius: 3px;
  cursor: pointer;
  font-size: 50px;
}

.site-button:hover {
  background-color: #2980b9;
}

</style>



  
