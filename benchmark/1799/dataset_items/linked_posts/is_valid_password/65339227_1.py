check('password')
    .notEmpty()
    .withMessage('Password cannot be null')
    .bail()
    .isLength({ min: 6 })
    .withMessage('Password must be at least 6 characters')
    .bail()
    .matches(/^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$/)
    .withMessage(
      'Must have atleast 1 uppercase, 1 lowercase letter and 1 number'
    ),
