--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.0
-- Dumped by pg_dump version 9.3.0
-- Started on 2013-09-22 17:30:35 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 175 (class 3079 OID 11756)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 1961 (class 0 OID 0)
-- Dependencies: 175
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 171 (class 1259 OID 16407)
-- Name: tbl_articles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbl_articles (
    article_id integer NOT NULL,
    article_first_id integer,
    article_last_id integer,
    article_status integer,
    article_permission integer
);


ALTER TABLE public.tbl_articles OWNER TO postgres;

--
-- TOC entry 170 (class 1259 OID 16405)
-- Name: tbl_articles_article_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tbl_articles_article_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbl_articles_article_id_seq OWNER TO postgres;

--
-- TOC entry 1962 (class 0 OID 0)
-- Dependencies: 170
-- Name: tbl_articles_article_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tbl_articles_article_id_seq OWNED BY tbl_articles.article_id;


--
-- TOC entry 172 (class 1259 OID 16413)
-- Name: tbl_articles_relative; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbl_articles_relative (
    artrev_page_id integer,
    artrev_index integer,
    artrev_article_id integer
);


ALTER TABLE public.tbl_articles_relative OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 16418)
-- Name: tbl_texts; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbl_texts (
    text_id integer NOT NULL,
    text_article_id integer,
    text_revision integer,
    text_source text,
    text_result text,
    text_user_id integer,
    text_iser_ip integer,
    text_date_create timestamp without time zone
);


ALTER TABLE public.tbl_texts OWNER TO postgres;

--
-- TOC entry 173 (class 1259 OID 16416)
-- Name: tbl_texts_text_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tbl_texts_text_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbl_texts_text_id_seq OWNER TO postgres;

--
-- TOC entry 1963 (class 0 OID 0)
-- Dependencies: 173
-- Name: tbl_texts_text_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tbl_texts_text_id_seq OWNED BY tbl_texts.text_id;


--
-- TOC entry 1838 (class 2604 OID 16410)
-- Name: article_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbl_articles ALTER COLUMN article_id SET DEFAULT nextval('tbl_articles_article_id_seq'::regclass);


--
-- TOC entry 1839 (class 2604 OID 16421)
-- Name: text_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbl_texts ALTER COLUMN text_id SET DEFAULT nextval('tbl_texts_text_id_seq'::regclass);


--
-- TOC entry 1950 (class 0 OID 16407)
-- Dependencies: 171
-- Data for Name: tbl_articles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tbl_articles (article_id, article_first_id, article_last_id, article_status, article_permission) FROM stdin;
\.


--
-- TOC entry 1964 (class 0 OID 0)
-- Dependencies: 170
-- Name: tbl_articles_article_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tbl_articles_article_id_seq', 1, false);


--
-- TOC entry 1951 (class 0 OID 16413)
-- Dependencies: 172
-- Data for Name: tbl_articles_relative; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tbl_articles_relative (artrev_page_id, artrev_index, artrev_article_id) FROM stdin;
\.


--
-- TOC entry 1953 (class 0 OID 16418)
-- Dependencies: 174
-- Data for Name: tbl_texts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tbl_texts (text_id, text_article_id, text_revision, text_source, text_result, text_user_id, text_iser_ip, text_date_create) FROM stdin;
\.


--
-- TOC entry 1965 (class 0 OID 0)
-- Dependencies: 173
-- Name: tbl_texts_text_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tbl_texts_text_id_seq', 1, false);


--
-- TOC entry 1841 (class 2606 OID 16412)
-- Name: tbl_articles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbl_articles
    ADD CONSTRAINT tbl_articles_pkey PRIMARY KEY (article_id);


--
-- TOC entry 1960 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2013-09-22 17:30:35 UTC

--
-- PostgreSQL database dump complete
--

