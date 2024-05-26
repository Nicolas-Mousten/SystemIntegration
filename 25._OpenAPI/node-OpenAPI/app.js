import express from "express";
const app = express();

import swaggerJSDoc from "swagger-jsdoc";
const swaggerDefinition = {
    failOnErrors: true, // Whether or not to throw when parsing errors. Defaults to false.
    definition: {
        openapi: '3.1.0',
        info: {
            title: 'Users Api',
            version: '0.0.1',
        },
    },
};
const swaggerOptions = {
    swaggerDefinition,
    apis: ["./routers/*.js"],
}

import swaggerUi from "swagger-ui-express";
app.use('/docs', swaggerUi.serve, swaggerUi.setup(swaggerJSDoc(swaggerOptions)));


import usersRouter from "./routers/usersRouter.js";
app.use(usersRouter);

const PORT = process.env.PORT ?? 8080;
app.listen(PORT, () => console.log("Server is running on port: ", PORT));


