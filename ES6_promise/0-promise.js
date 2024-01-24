// Exports a function that simulates an API response
export default function getResponseFromAPI() {
  // Return a promise
  return new Promise((resolve) => {
    // Resolve the promise after 1 second
    setTimeout(() => resolve('API response'), 1000);
  });
}
