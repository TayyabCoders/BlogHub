import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./ui_components/Layout";
import Home from "./pages/Home";
import Detail from "./pages/Detail";
import Signup from "./pages/Signup";
import CreatePost from "./pages/CreatePost";
import Login from "./pages/Login";
import ProtectedRoute from "./ui_components/ProtectedRoute";
import { useEffect, useState } from "react";
import { getUsername } from "./services/apiBlog";
import { useQuery } from "@tanstack/react-query";
import Profile from "./pages/Profile";
import NotFound from "./pages/NotFound";

const App = () => {
  const [username, setUsername] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const { data } = useQuery({
    queryKey: ["username"],
    queryFn: getUsername,
  });

  useEffect(
    function () {
      if (data) {
        setUsername(data.username);
        setIsAuthenticated(true);
      }
    },
    [data]
  );

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <Layout
              isAuthenticated={isAuthenticated}
              username={username}
              setUsername={setUsername}
              setIsAuthenticated={setIsAuthenticated}
            />
          }
        >
          <Route index element={<Home />} />
          <Route path="*" element={<NotFound/>} />
          <Route path="profile/:username" element={<Profile authUsername={username}/>} />
          <Route path="blogs/:slug" element={<Detail username={username} isAuthenticated={isAuthenticated} />} />
          <Route path="signup" element={<Signup />} />
          <Route
            path="create"
            element={
              <ProtectedRoute>
                <CreatePost />
              </ProtectedRoute>
            }
          />
          <Route
            path="signin"
            element={
              <Login
                setIsAuthenticated={setIsAuthenticated}
                setUsername={setUsername}
              />
            }
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;