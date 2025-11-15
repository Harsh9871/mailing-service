import express from "express";
import mailRoutes from "./routes/mail.routes.js";

const app = express();
app.use(express.static("public"));

const PORT = process.env.PORT || 3100;

app.use(express.json());

app.use("/api/mail", mailRoutes);

app.listen(PORT, () => {
    console.log(`Mailing microservice running on port ${PORT}`);
});
