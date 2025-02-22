const pTagSelector = "p";
const loader = new CheerioWebBaseLoader(
  "https://lilianweng.github.io/posts/2023-06-23-agent/",
  {
    selector: pTagSelector,
  }
);

const docs = await loader.load();
console.log(docs[0].pageContent.length);