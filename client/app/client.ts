const baseUrl = "localhost:5000/doot";

export const getData = async () => {
  try {
    const response = await fetch(baseUrl);

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (err) {
    console.error(err);
  }
};
