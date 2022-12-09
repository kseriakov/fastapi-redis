import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Orders } from "./components/Orders";
import { ProductCreate } from "./components/ProductCreate";
import { Products } from "./components/Products";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        children: [
            {
                index: true,
                element: <Products />,
            },
            {
                path: "create",
                element: <ProductCreate />,
            },
            {
                path: "order",
                element: <Orders />,
            },
        ],
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
