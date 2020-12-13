--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: games; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.games (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.games OWNER TO postgres;

--
-- Name: games_encounters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.games_encounters (
    encounterid integer NOT NULL,
    gameid integer NOT NULL,
    eid integer NOT NULL
);


ALTER TABLE public.games_encounters OWNER TO postgres;

--
-- Name: games_encounters_eid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.games_encounters_eid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_encounters_eid_seq OWNER TO postgres;

--
-- Name: games_encounters_eid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.games_encounters_eid_seq OWNED BY public.games_encounters.eid;


--
-- Name: games_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.games_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_id_seq OWNER TO postgres;

--
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.games_id_seq OWNED BY public.games.id;


--
-- Name: games_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.games_users (
    gid integer NOT NULL,
    uid integer NOT NULL,
    creator boolean DEFAULT false,
    charname text
);


ALTER TABLE public.games_users OWNER TO postgres;

--
-- Name: initiative; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.initiative (
    eid integer,
    uid integer,
    initnum integer
);


ALTER TABLE public.initiative OWNER TO postgres;

--
-- Name: monsters_initiative; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters_initiative (
    id integer NOT NULL,
    eid integer,
    monstername text,
    initiative integer
);


ALTER TABLE public.monsters_initiative OWNER TO postgres;

--
-- Name: monsters_initiative_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_initiative_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.monsters_initiative_id_seq OWNER TO postgres;

--
-- Name: monsters_initiative_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_initiative_id_seq OWNED BY public.monsters_initiative.id;


--
-- Name: powers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.powers (
    id integer NOT NULL,
    name text,
    description text
);


ALTER TABLE public.powers OWNER TO postgres;

--
-- Name: powers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.powers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.powers_id_seq OWNER TO postgres;

--
-- Name: powers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.powers_id_seq OWNED BY public.powers.id;


--
-- Name: powers_players; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.powers_players (
    pid integer,
    uid integer,
    gid integer
);


ALTER TABLE public.powers_players OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text,
    password text,
    admin boolean DEFAULT false
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: games id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games ALTER COLUMN id SET DEFAULT nextval('public.games_id_seq'::regclass);


--
-- Name: games_encounters eid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_encounters ALTER COLUMN eid SET DEFAULT nextval('public.games_encounters_eid_seq'::regclass);


--
-- Name: monsters_initiative id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_initiative ALTER COLUMN id SET DEFAULT nextval('public.monsters_initiative_id_seq'::regclass);


--
-- Name: powers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.powers ALTER COLUMN id SET DEFAULT nextval('public.powers_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: games_encounters eid; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_encounters
    ADD CONSTRAINT eid UNIQUE (eid);


--
-- Name: games_encounters games_encounters_encounterid_gameid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_encounters
    ADD CONSTRAINT games_encounters_encounterid_gameid_key UNIQUE (encounterid, gameid);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (id);


--
-- Name: games_users games_users_gid_uid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_users
    ADD CONSTRAINT games_users_gid_uid_key UNIQUE (gid, uid);


--
-- Name: initiative initiative_eid_uid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.initiative
    ADD CONSTRAINT initiative_eid_uid_key UNIQUE (eid, uid);


--
-- Name: monsters_initiative monsters_initiative_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_initiative
    ADD CONSTRAINT monsters_initiative_pkey PRIMARY KEY (id);


--
-- Name: powers powers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.powers
    ADD CONSTRAINT powers_pkey PRIMARY KEY (id);


--
-- Name: users username; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT username UNIQUE (username);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: initiative eid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.initiative
    ADD CONSTRAINT eid FOREIGN KEY (eid) REFERENCES public.games_encounters(eid) ON DELETE CASCADE;


--
-- Name: monsters_initiative eid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_initiative
    ADD CONSTRAINT eid FOREIGN KEY (eid) REFERENCES public.games_encounters(eid) ON DELETE CASCADE;


--
-- Name: games_encounters gameid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_encounters
    ADD CONSTRAINT gameid FOREIGN KEY (gameid) REFERENCES public.games(id) ON DELETE CASCADE;


--
-- Name: games_users games_users_gid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_users
    ADD CONSTRAINT games_users_gid_fkey FOREIGN KEY (gid) REFERENCES public.games(id) ON DELETE CASCADE;


--
-- Name: games_users games_users_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.games_users
    ADD CONSTRAINT games_users_uid_fkey FOREIGN KEY (uid) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: powers_players gid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.powers_players
    ADD CONSTRAINT gid FOREIGN KEY (gid) REFERENCES public.games(id) ON DELETE CASCADE;


--
-- Name: powers_players pid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.powers_players
    ADD CONSTRAINT pid FOREIGN KEY (pid) REFERENCES public.powers(id) ON DELETE CASCADE;


--
-- Name: initiative uid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.initiative
    ADD CONSTRAINT uid FOREIGN KEY (uid) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: powers_players uid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.powers_players
    ADD CONSTRAINT uid FOREIGN KEY (uid) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

