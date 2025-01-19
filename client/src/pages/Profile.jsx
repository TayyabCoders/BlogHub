import { getUserInfo } from "@/services/apiBlog";
import BlogContainer from "@/ui_components/BlogContainer";
import Hero from "@/ui_components/Hero";
import Spinner from "@/ui_components/Spinner";
import Modal from "@/ui_components/Modal";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import Signup from "./Signup";
import { useState } from "react";

const Profile = ({ authUsername }) => {
  const [showModal, setShowModal] = useState(false);

  const toggleModal = () => {
    setShowModal(curr => !curr)
  }


  const { username } = useParams();

  const { isPending, data } = useQuery({
    queryKey: ["users", username],
    queryFn: () => getUserInfo(username),
  });

  const blogs = data?.author_posts;

  if (isPending) {
    return <Spinner />;
  }

  return (
    <>
      <Hero userInfo={data} authUsername={authUsername} toggleModal={toggleModal} />
      <BlogContainer blogs={blogs} title={`🍔 ${username}'s Posts`} />

      {showModal && (
        <Modal toggleModal={toggleModal}>
          <Signup userInfo={data} updateForm={true} toggleModal={toggleModal} />
        </Modal>
      )}
    </>
  );
};

export default Profile;