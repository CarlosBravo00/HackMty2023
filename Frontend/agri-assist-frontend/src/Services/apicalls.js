import axios from "axios";

const apiUrl = "https://37e8dwyhx3.execute-api.us-west-2.amazonaws.com/";
const searchUrl = "http://127.0.0.1:5000/search";

async function postData(query) {
  try {
    const response = await axios.post(searchUrl, {
      query: query,
    });

    if (response.status !== 200) {
      throw new Error(`Network response was not ok, status code: ${response.status}`);
    }

    return response.data;
  } catch (error) {
    throw error;
  }
}


async function fetchData() {
  try {
    const response = await axios.get(apiUrl + "getData");

    if (response.status !== 200) {
      throw new Error(
        `Network response was not ok, status code: ${response.status}`
      );
    }

    return response.data;
  } catch (error) {
    throw error;
  }
}

export { fetchData, postData };
