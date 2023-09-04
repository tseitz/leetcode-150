const airports = ["PHX", "LAX", "JFK", "OKC", "MEX"];

const routes = [
  ["PHX", "LAX"],
  ["PHX", "JFK"],
  ["JFK", "OKC"],
  ["MEX", "LAX"],
];

const adjacencyList = new Map();

function addNode(airport) {
  adjacencyList.set(airport, []);
}

function addEdge(origin, destination) {
  adjacencyList.get(origin).push(destination);
  adjacencyList.get(destination).push(origin);
}

airports.forEach(addNode);
routes.forEach((route) => addEdge(...route));
