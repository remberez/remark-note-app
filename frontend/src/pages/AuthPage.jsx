import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import logo from "../assets/logo.png";
import AuthService from '../services/AuthService';
import authStore from '../store/authStore';
import { observer } from "mobx-react-lite";

const AuthPage = () => {
    const initialValues = {
        email: '',
        password: '',
    };

    const validationSchema = Yup.object({
        email: Yup.string()
            .email('Некорректный email адрес')
            .required('Обязательное поле'),
        password: Yup.string()
            .min(3, 'Пароль должен быть не менее 6 символов')
            .required('Обязательное поле'),
    });

    console.log(authStore.isAuth);
    const onSubmit = async (values, { setSubmitting }) => {
        const token = await AuthService.login(values.email, values.password)
        authStore.setToken(token);
    };

    return (
        <section className="bg-pageColor h-[100vh] flex items-center justify-center flex-col font-unbounded">
            <img
                src={logo}
                width={100}
                height={100}
                className="mb-5"
                alt="Логотип"
            />
            <h1 className="text-white text-xl mb-5">
                Войдите в свой аккаунт
            </h1>
            <Formik
                initialValues={initialValues}
                validationSchema={validationSchema}
                onSubmit={onSubmit}
            >
                {({ isSubmitting }) => (
                    <Form className="flex flex-col w-[350px]">
                        <label htmlFor="email" className="text-white mb-2">
                            Email
                        </label>
                        <Field
                            type="email"
                            name="email"
                            className="mb-4 p-2 rounded"
                        />
                        <ErrorMessage name="email" component="div" className="text-red-500 text-xs mb-4" />
                        <label htmlFor="password" className="text-white mb-2">
                            Пароль
                        </label>
                        <Field
                            type="password"
                            name="password"
                            className="mb-4 p-2 rounded"
                        />
                        <ErrorMessage name="password" component="div" className="text-red-500 text-xs mb-4" />
                        <button
                            type="submit"
                            disabled={isSubmitting}
                            className="bg-green text-white p-2 rounded"
                        >
                            Войти
                        </button>
                    </Form>
                )}
            </Formik>
        </section>
    );
};

export default observer(AuthPage);