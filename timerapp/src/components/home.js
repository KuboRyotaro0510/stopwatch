import { Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <h1>ストップウォッチアプリ</h1>
      <div>
        ログインは<Link to={`/login/`}>こちら</Link>
      </div>
    </>
  );
};

export default Home;
