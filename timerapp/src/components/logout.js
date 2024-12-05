import { useAuth } from "../AuthContext";

function Logout() {
  const { logout } = useAuth();
  const handleLogout = () => {
    logout();
  };

  return <button onClick={handleLogout}>ログアウト</button>;
}

export default Logout;
