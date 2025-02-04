import { useState } from "react";
import { getBlogs } from "@/services/apiBlog";
import BlogContainer from "@/ui_components/BlogContainer";
import Header from "@/ui_components/Header";
import PagePagination from "../ui_components/PagePagination";
import { useQuery, keepPreviousData } from "@tanstack/react-query";

const Home = () => {
  const [page, setPage] = useState(1);
  const numOfBlogsPerPage = 1;

  const { isPending, isError, error, data } = useQuery({
    queryKey: ["blogs", page],
    queryFn: () => getBlogs(page),
    placeholderData: keepPreviousData,
  });
  console.log(data)
  const blogs = data?.results || [];
  console.log(blogs)
  const numOfPages = Math.ceil(data?.count / numOfBlogsPerPage);

  function handleSetPage(val) {
    setPage(val);
  }

  function increasePageValue() {
    setPage((curr) => curr + 1);
  }

  function decreasePageValue() {
    setPage((curr) => curr - 1);
  }

  return (
    <>
      <Header />
      <BlogContainer isPending={isPending} blogs={blogs} />
      <PagePagination
        increasePageValue={increasePageValue}
        decreasePageValue={decreasePageValue}
        page={page}
        numOfPages={numOfPages}
        handleSetPage={handleSetPage}
      />
    </>
  );
};

export default Home;