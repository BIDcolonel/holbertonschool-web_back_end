export default function getResponseFromAPI() {
    return new Promise((resolve) => {
      setTimeout(() => resolve("Réponse de l'API"), 1000);
    });
  }
