import { Router } from "express"
const router = Router();

let currentId = 2
const users = [
    {id: 1, name: "Alice"},
    {id: 2, name: "Bob"}
];


/**
 * @openapi
 * /api/users:
 *   get:
 *     description: Get all users
 *     responses:
 *       200:
 *         description: Return all users.
 */
router.get("/api/users", (req, res) =>{
    res.send({data: users});
});


/**
 * @openapi
 * /api/users:
 *   post:
 *     description: Create a new user
 *     responses:
 *       200:
 *         description: Returns the users that was created
 * 
 */
router.post("api/users", (req, res) => {
    const newUser = req.body;
    newUser.id = ++currentId;
    users.push(newUser);

    res.send({data: newUser });
})

export default router;