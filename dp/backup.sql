PGDMP     3    +                 x            master    9.5.19    9.5.19 �    X	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            Y	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            Z	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            [	           1262    55142    master    DATABASE     l   CREATE DATABASE master WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_IN' LC_CTYPE = 'en_IN';
    DROP DATABASE master;
             sushil    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            \	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    6            ]	           0    0    SCHEMA public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    6                        3079    12393    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            ^	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    55156    DDB_aggregate_tc_state    TABLE     �   CREATE TABLE public."DDB_aggregate_tc_state" (
    id integer NOT NULL,
    "Domain" character varying(50) NOT NULL,
    "Total" integer NOT NULL,
    "Automated" integer NOT NULL,
    "Pass" integer NOT NULL,
    "Fail" integer NOT NULL
);
 ,   DROP TABLE public."DDB_aggregate_tc_state";
       public         sushil    false    6            �            1259    55154    DDB_aggregate_tc_state_id_seq    SEQUENCE     �   CREATE SEQUENCE public."DDB_aggregate_tc_state_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public."DDB_aggregate_tc_state_id_seq";
       public       sushil    false    184    6            _	           0    0    DDB_aggregate_tc_state_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public."DDB_aggregate_tc_state_id_seq" OWNED BY public."DDB_aggregate_tc_state".id;
            public       sushil    false    183            �            1259    55164    DDB_default_values    TABLE     H  CREATE TABLE public."DDB_default_values" (
    id integer NOT NULL,
    "CardType" character varying(20)[] NOT NULL,
    "ServerType" character varying(20)[] NOT NULL,
    "StatusValues" character varying(20)[] NOT NULL,
    "UserRoles" character varying(20)[] NOT NULL,
    "UserPermission" character varying(20)[] NOT NULL
);
 (   DROP TABLE public."DDB_default_values";
       public         sushil    false    6            �            1259    55162    DDB_default_values_id_seq    SEQUENCE     �   CREATE SEQUENCE public."DDB_default_values_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public."DDB_default_values_id_seq";
       public       sushil    false    186    6            `	           0    0    DDB_default_values_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."DDB_default_values_id_seq" OWNED BY public."DDB_default_values".id;
            public       sushil    false    185            �            1259    55175    DDB_logs    TABLE       CREATE TABLE public."DDB_logs" (
    "logNo" integer NOT NULL,
    "UserName" character varying(100) NOT NULL,
    "Timestamp" timestamp with time zone NOT NULL,
    "RequestType" character varying(10) NOT NULL,
    "LogData" text NOT NULL,
    "URL" character varying(100)
);
    DROP TABLE public."DDB_logs";
       public         sushil    false    6            �            1259    55173    DDB_logs_logNo_seq    SEQUENCE     }   CREATE SEQUENCE public."DDB_logs_logNo_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public."DDB_logs_logNo_seq";
       public       sushil    false    6    188            a	           0    0    DDB_logs_logNo_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public."DDB_logs_logNo_seq" OWNED BY public."DDB_logs"."logNo";
            public       sushil    false    187            �            1259    55184    DDB_releases    TABLE     �  CREATE TABLE public."DDB_releases" (
    "ReleaseNumber" character varying(10) NOT NULL,
    "BuildNumberList" character varying(15)[] NOT NULL,
    "EngineerCount" integer NOT NULL,
    "CardType" character varying(100)[] NOT NULL,
    "ServerType" character varying(100)[] NOT NULL,
    "SetupsUsed" character varying(100)[] NOT NULL,
    "QAStartDate" timestamp with time zone,
    "TargetedReleaseDate" timestamp with time zone,
    "ActualReleaseDate" timestamp with time zone,
    "TargetedCodeFreezeDate" timestamp with time zone,
    "UpgradeTestingStartDate" timestamp with time zone,
    "UpgradeMetrics" character varying(100)[],
    "Customers" character varying(100)[] NOT NULL,
    "FinalBuild" character varying(100) NOT NULL,
    "FinalOS" character varying(100) NOT NULL,
    "FinalDockerCore" character varying(100) NOT NULL,
    "UbootVersion" character varying(100) NOT NULL,
    "RedFlagsRisks" text NOT NULL,
    "AutomationSyncUp" text NOT NULL,
    "QARateOfProgress" integer NOT NULL
);
 "   DROP TABLE public."DDB_releases";
       public         sushil    false    6            �            1259    55240    DDB_sanity_results    TABLE     L  CREATE TABLE public."DDB_sanity_results" (
    "SanityId" integer NOT NULL,
    "Tag" character varying(6) NOT NULL,
    "Build" character varying(10) NOT NULL,
    "Result" character varying(10) NOT NULL,
    "Logs" text NOT NULL,
    "Timestamp" timestamp with time zone NOT NULL,
    "Setup_id" character varying(20) NOT NULL
);
 (   DROP TABLE public."DDB_sanity_results";
       public         sushil    false    6            �            1259    55238    DDB_sanity_results_SanityId_seq    SEQUENCE     �   CREATE SEQUENCE public."DDB_sanity_results_SanityId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."DDB_sanity_results_SanityId_seq";
       public       sushil    false    199    6            b	           0    0    DDB_sanity_results_SanityId_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public."DDB_sanity_results_SanityId_seq" OWNED BY public."DDB_sanity_results"."SanityId";
            public       sushil    false    198            �            1259    55230    DDB_setup_info    TABLE     Z  CREATE TABLE public."DDB_setup_info" (
    "SetupName" character varying(20) NOT NULL,
    "Inventory" character varying(5000) NOT NULL,
    "ClusterState" character varying(6) NOT NULL,
    "ClusterStatus" character varying(6) NOT NULL,
    "CurrentUserId_id" character varying(100) NOT NULL,
    "OwnerId_id" character varying(100) NOT NULL
);
 $   DROP TABLE public."DDB_setup_info";
       public         sushil    false    6            �            1259    55194    DDB_tc_info    TABLE     a  CREATE TABLE public."DDB_tc_info" (
    id integer NOT NULL,
    "TcID" character varying(200) NOT NULL,
    "TcName" character varying(2000) NOT NULL,
    "Domain" character varying(50) NOT NULL,
    "SubDomain" character varying(50) NOT NULL,
    "Scenario" character varying(200) NOT NULL,
    "Description" text NOT NULL,
    "ExpectedBehaviour" character varying(5000) NOT NULL,
    "Notes" character varying(2000) NOT NULL,
    "CardType" character varying(100) NOT NULL,
    "ServerType" character varying(10)[] NOT NULL,
    "OrchestrationPlatform" character varying(10)[] NOT NULL,
    "Status" character varying(50) NOT NULL,
    "Date" timestamp with time zone NOT NULL,
    "Assignee" character varying(50) NOT NULL,
    "Creator" character varying(50) NOT NULL,
    "Tag" character varying(20) NOT NULL,
    "Priority" character varying(3) NOT NULL
);
 !   DROP TABLE public."DDB_tc_info";
       public         sushil    false    6            �            1259    55192    DDB_tc_info_id_seq    SEQUENCE     }   CREATE SEQUENCE public."DDB_tc_info_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public."DDB_tc_info_id_seq";
       public       sushil    false    6    191            c	           0    0    DDB_tc_info_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public."DDB_tc_info_id_seq" OWNED BY public."DDB_tc_info".id;
            public       sushil    false    190            �            1259    55205    DDB_tc_status    TABLE     �  CREATE TABLE public."DDB_tc_status" (
    id integer NOT NULL,
    "TcID" character varying(200) NOT NULL,
    "TcName" character varying(2000) NOT NULL,
    "Build" character varying(1000) NOT NULL,
    "Result" character varying(14) NOT NULL,
    "Bugs" character varying(500) NOT NULL,
    "Date" timestamp with time zone,
    "Domain" character varying(50) NOT NULL,
    "SubDomain" character varying(50) NOT NULL,
    "CardType" character varying(10) NOT NULL
);
 #   DROP TABLE public."DDB_tc_status";
       public         sushil    false    6            �            1259    55216    DDB_tc_status_gui    TABLE     �  CREATE TABLE public."DDB_tc_status_gui" (
    id integer NOT NULL,
    "TcID" character varying(200) NOT NULL,
    "BuildUbuntuChrome" character varying(20) NOT NULL,
    "BuildUbuntuFirefox" character varying(20) NOT NULL,
    "BuildWindowsChrome" character varying(20) NOT NULL,
    "BuildWindowsFirefox" character varying(20) NOT NULL,
    "BuildWindowsIE" character varying(20) NOT NULL,
    "BuildMacSafari" character varying(20) NOT NULL,
    "ResultUbuntuChrome" character varying(20) NOT NULL,
    "ResultUbuntuFirefox" character varying(20) NOT NULL,
    "ResultWindowsIE" character varying(20) NOT NULL,
    "ResultWindowsChrome" character varying(20) NOT NULL,
    "ResultWindowsFirefox" character varying(20) NOT NULL,
    "ResultMacSafari" character varying(20) NOT NULL,
    "Bug" character varying(500) NOT NULL,
    "Date" timestamp with time zone NOT NULL,
    "Domain" character varying(50) NOT NULL,
    "SubDomain" character varying(50) NOT NULL,
    "CardType" character varying(10) NOT NULL
);
 '   DROP TABLE public."DDB_tc_status_gui";
       public         sushil    false    6            �            1259    55214    DDB_tc_status_gui_id_seq    SEQUENCE     �   CREATE SEQUENCE public."DDB_tc_status_gui_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."DDB_tc_status_gui_id_seq";
       public       sushil    false    195    6            d	           0    0    DDB_tc_status_gui_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public."DDB_tc_status_gui_id_seq" OWNED BY public."DDB_tc_status_gui".id;
            public       sushil    false    194            �            1259    55203    DDB_tc_status_id_seq    SEQUENCE        CREATE SEQUENCE public."DDB_tc_status_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public."DDB_tc_status_id_seq";
       public       sushil    false    193    6            e	           0    0    DDB_tc_status_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public."DDB_tc_status_id_seq" OWNED BY public."DDB_tc_status".id;
            public       sushil    false    192            �            1259    55225    DDB_user_info    TABLE     �   CREATE TABLE public."DDB_user_info" (
    "UserName" character varying(100) NOT NULL,
    "Role" character varying(10) NOT NULL,
    "Name" character varying(100) NOT NULL
);
 #   DROP TABLE public."DDB_user_info";
       public         sushil    false    6            �            1259    55354 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         sushil    false    6            �            1259    55352    auth_group_id_seq    SEQUENCE     z   CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       sushil    false    205    6            f	           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public       sushil    false    204            �            1259    55364    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         sushil    false    6            �            1259    55362    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       sushil    false    207    6            g	           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public       sushil    false    206            �            1259    55346    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         sushil    false    6            �            1259    55344    auth_permission_id_seq    SEQUENCE        CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       sushil    false    203    6            h	           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public       sushil    false    202            �            1259    55372 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         sushil    false    6            �            1259    55382    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         sushil    false    6            �            1259    55380    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       sushil    false    211    6            i	           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
            public       sushil    false    210            �            1259    55370    auth_user_id_seq    SEQUENCE     y   CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       sushil    false    6    209            j	           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
            public       sushil    false    208            �            1259    55390    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         sushil    false    6            �            1259    55388 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       sushil    false    6    213            k	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
            public       sushil    false    212            �            1259    55450    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         sushil    false    6            �            1259    55448    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       sushil    false    6    215            l	           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public       sushil    false    214            �            1259    55336    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         sushil    false    6            �            1259    55334    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       sushil    false    201    6            m	           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public       sushil    false    200            �            1259    55145    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         sushil    false    6            �            1259    55143    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       sushil    false    6    182            n	           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public       sushil    false    181            �            1259    55481    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         sushil    false    6            X           2604    55159    id    DEFAULT     �   ALTER TABLE ONLY public."DDB_aggregate_tc_state" ALTER COLUMN id SET DEFAULT nextval('public."DDB_aggregate_tc_state_id_seq"'::regclass);
 J   ALTER TABLE public."DDB_aggregate_tc_state" ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    183    184    184            Y           2604    55167    id    DEFAULT     �   ALTER TABLE ONLY public."DDB_default_values" ALTER COLUMN id SET DEFAULT nextval('public."DDB_default_values_id_seq"'::regclass);
 F   ALTER TABLE public."DDB_default_values" ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    186    185    186            Z           2604    55178    logNo    DEFAULT     v   ALTER TABLE ONLY public."DDB_logs" ALTER COLUMN "logNo" SET DEFAULT nextval('public."DDB_logs_logNo_seq"'::regclass);
 A   ALTER TABLE public."DDB_logs" ALTER COLUMN "logNo" DROP DEFAULT;
       public       sushil    false    187    188    188            ^           2604    55243    SanityId    DEFAULT     �   ALTER TABLE ONLY public."DDB_sanity_results" ALTER COLUMN "SanityId" SET DEFAULT nextval('public."DDB_sanity_results_SanityId_seq"'::regclass);
 N   ALTER TABLE public."DDB_sanity_results" ALTER COLUMN "SanityId" DROP DEFAULT;
       public       sushil    false    198    199    199            [           2604    55197    id    DEFAULT     t   ALTER TABLE ONLY public."DDB_tc_info" ALTER COLUMN id SET DEFAULT nextval('public."DDB_tc_info_id_seq"'::regclass);
 ?   ALTER TABLE public."DDB_tc_info" ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    190    191    191            \           2604    55208    id    DEFAULT     x   ALTER TABLE ONLY public."DDB_tc_status" ALTER COLUMN id SET DEFAULT nextval('public."DDB_tc_status_id_seq"'::regclass);
 A   ALTER TABLE public."DDB_tc_status" ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    192    193    193            ]           2604    55219    id    DEFAULT     �   ALTER TABLE ONLY public."DDB_tc_status_gui" ALTER COLUMN id SET DEFAULT nextval('public."DDB_tc_status_gui_id_seq"'::regclass);
 E   ALTER TABLE public."DDB_tc_status_gui" ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    194    195    195            a           2604    55357    id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    205    204    205            b           2604    55367    id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    207    206    207            `           2604    55349    id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    203    202    203            c           2604    55375    id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    209    208    209            d           2604    55385    id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    211    210    211            e           2604    55393    id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    212    213    213            f           2604    55453    id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    214    215    215            _           2604    55339    id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    200    201    201            W           2604    55148    id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       sushil    false    181    182    182            5	          0    55156    DDB_aggregate_tc_state 
   TABLE DATA               f   COPY public."DDB_aggregate_tc_state" (id, "Domain", "Total", "Automated", "Pass", "Fail") FROM stdin;
    public       sushil    false    184   6�       o	           0    0    DDB_aggregate_tc_state_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public."DDB_aggregate_tc_state_id_seq"', 1, false);
            public       sushil    false    183            7	          0    55164    DDB_default_values 
   TABLE DATA               {   COPY public."DDB_default_values" (id, "CardType", "ServerType", "StatusValues", "UserRoles", "UserPermission") FROM stdin;
    public       sushil    false    186   S�       p	           0    0    DDB_default_values_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."DDB_default_values_id_seq"', 1, false);
            public       sushil    false    185            9	          0    55175    DDB_logs 
   TABLE DATA               g   COPY public."DDB_logs" ("logNo", "UserName", "Timestamp", "RequestType", "LogData", "URL") FROM stdin;
    public       sushil    false    188   p�       q	           0    0    DDB_logs_logNo_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."DDB_logs_logNo_seq"', 1, false);
            public       sushil    false    187            :	          0    55184    DDB_releases 
   TABLE DATA               �  COPY public."DDB_releases" ("ReleaseNumber", "BuildNumberList", "EngineerCount", "CardType", "ServerType", "SetupsUsed", "QAStartDate", "TargetedReleaseDate", "ActualReleaseDate", "TargetedCodeFreezeDate", "UpgradeTestingStartDate", "UpgradeMetrics", "Customers", "FinalBuild", "FinalOS", "FinalDockerCore", "UbootVersion", "RedFlagsRisks", "AutomationSyncUp", "QARateOfProgress") FROM stdin;
    public       sushil    false    189   ��       D	          0    55240    DDB_sanity_results 
   TABLE DATA               u   COPY public."DDB_sanity_results" ("SanityId", "Tag", "Build", "Result", "Logs", "Timestamp", "Setup_id") FROM stdin;
    public       sushil    false    199   ��       r	           0    0    DDB_sanity_results_SanityId_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."DDB_sanity_results_SanityId_seq"', 1, false);
            public       sushil    false    198            B	          0    55230    DDB_setup_info 
   TABLE DATA               �   COPY public."DDB_setup_info" ("SetupName", "Inventory", "ClusterState", "ClusterStatus", "CurrentUserId_id", "OwnerId_id") FROM stdin;
    public       sushil    false    197   ��       <	          0    55194    DDB_tc_info 
   TABLE DATA               �   COPY public."DDB_tc_info" (id, "TcID", "TcName", "Domain", "SubDomain", "Scenario", "Description", "ExpectedBehaviour", "Notes", "CardType", "ServerType", "OrchestrationPlatform", "Status", "Date", "Assignee", "Creator", "Tag", "Priority") FROM stdin;
    public       sushil    false    191   ��       s	           0    0    DDB_tc_info_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."DDB_tc_info_id_seq"', 1, false);
            public       sushil    false    190            >	          0    55205    DDB_tc_status 
   TABLE DATA               �   COPY public."DDB_tc_status" (id, "TcID", "TcName", "Build", "Result", "Bugs", "Date", "Domain", "SubDomain", "CardType") FROM stdin;
    public       sushil    false    193   �       @	          0    55216    DDB_tc_status_gui 
   TABLE DATA               i  COPY public."DDB_tc_status_gui" (id, "TcID", "BuildUbuntuChrome", "BuildUbuntuFirefox", "BuildWindowsChrome", "BuildWindowsFirefox", "BuildWindowsIE", "BuildMacSafari", "ResultUbuntuChrome", "ResultUbuntuFirefox", "ResultWindowsIE", "ResultWindowsChrome", "ResultWindowsFirefox", "ResultMacSafari", "Bug", "Date", "Domain", "SubDomain", "CardType") FROM stdin;
    public       sushil    false    195   �       t	           0    0    DDB_tc_status_gui_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public."DDB_tc_status_gui_id_seq"', 1, false);
            public       sushil    false    194            u	           0    0    DDB_tc_status_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."DDB_tc_status_id_seq"', 1, false);
            public       sushil    false    192            A	          0    55225    DDB_user_info 
   TABLE DATA               E   COPY public."DDB_user_info" ("UserName", "Role", "Name") FROM stdin;
    public       sushil    false    196   ;�       J	          0    55354 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public       sushil    false    205   X�       v	           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
            public       sushil    false    204            L	          0    55364    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       sushil    false    207   u�       w	           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
            public       sushil    false    206            H	          0    55346    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       sushil    false    203   ��       x	           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 64, true);
            public       sushil    false    202            N	          0    55372 	   auth_user 
   TABLE DATA               �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       sushil    false    209   ;�       P	          0    55382    auth_user_groups 
   TABLE DATA               A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public       sushil    false    211   X�       y	           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
            public       sushil    false    210            z	           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);
            public       sushil    false    208            R	          0    55390    auth_user_user_permissions 
   TABLE DATA               P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       sushil    false    213   u�       {	           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
            public       sushil    false    212            T	          0    55450    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       sushil    false    215   ��       |	           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
            public       sushil    false    214            F	          0    55336    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public       sushil    false    201   ��       }	           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 16, true);
            public       sushil    false    200            3	          0    55145    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public       sushil    false    182   s�       ~	           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 27, true);
            public       sushil    false    181            U	          0    55481    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public       sushil    false    216   ��       k           2606    55161    DDB_aggregate_tc_state_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public."DDB_aggregate_tc_state"
    ADD CONSTRAINT "DDB_aggregate_tc_state_pkey" PRIMARY KEY (id);
 `   ALTER TABLE ONLY public."DDB_aggregate_tc_state" DROP CONSTRAINT "DDB_aggregate_tc_state_pkey";
       public         sushil    false    184    184            m           2606    55172    DDB_default_values_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public."DDB_default_values"
    ADD CONSTRAINT "DDB_default_values_pkey" PRIMARY KEY (id);
 X   ALTER TABLE ONLY public."DDB_default_values" DROP CONSTRAINT "DDB_default_values_pkey";
       public         sushil    false    186    186            o           2606    55183    DDB_logs_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."DDB_logs"
    ADD CONSTRAINT "DDB_logs_pkey" PRIMARY KEY ("logNo");
 D   ALTER TABLE ONLY public."DDB_logs" DROP CONSTRAINT "DDB_logs_pkey";
       public         sushil    false    188    188            r           2606    55191    DDB_releases_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public."DDB_releases"
    ADD CONSTRAINT "DDB_releases_pkey" PRIMARY KEY ("ReleaseNumber");
 L   ALTER TABLE ONLY public."DDB_releases" DROP CONSTRAINT "DDB_releases_pkey";
       public         sushil    false    189    189            �           2606    55248    DDB_sanity_results_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public."DDB_sanity_results"
    ADD CONSTRAINT "DDB_sanity_results_pkey" PRIMARY KEY ("SanityId");
 X   ALTER TABLE ONLY public."DDB_sanity_results" DROP CONSTRAINT "DDB_sanity_results_pkey";
       public         sushil    false    199    199            �           2606    55237    DDB_setup_info_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public."DDB_setup_info"
    ADD CONSTRAINT "DDB_setup_info_pkey" PRIMARY KEY ("SetupName");
 P   ALTER TABLE ONLY public."DDB_setup_info" DROP CONSTRAINT "DDB_setup_info_pkey";
       public         sushil    false    197    197            t           2606    55202    DDB_tc_info_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."DDB_tc_info"
    ADD CONSTRAINT "DDB_tc_info_pkey" PRIMARY KEY (id);
 J   ALTER TABLE ONLY public."DDB_tc_info" DROP CONSTRAINT "DDB_tc_info_pkey";
       public         sushil    false    191    191            x           2606    55224    DDB_tc_status_gui_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."DDB_tc_status_gui"
    ADD CONSTRAINT "DDB_tc_status_gui_pkey" PRIMARY KEY (id);
 V   ALTER TABLE ONLY public."DDB_tc_status_gui" DROP CONSTRAINT "DDB_tc_status_gui_pkey";
       public         sushil    false    195    195            v           2606    55213    DDB_tc_status_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public."DDB_tc_status"
    ADD CONSTRAINT "DDB_tc_status_pkey" PRIMARY KEY (id);
 N   ALTER TABLE ONLY public."DDB_tc_status" DROP CONSTRAINT "DDB_tc_status_pkey";
       public         sushil    false    193    193            {           2606    55229    DDB_user_info_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."DDB_user_info"
    ADD CONSTRAINT "DDB_user_info_pkey" PRIMARY KEY ("UserName");
 N   ALTER TABLE ONLY public."DDB_user_info" DROP CONSTRAINT "DDB_user_info_pkey";
       public         sushil    false    196    196            �           2606    55479    auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         sushil    false    205    205            �           2606    55416 ;   auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         sushil    false    207    207    207            �           2606    55369    auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         sushil    false    207    207            �           2606    55359    auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         sushil    false    205    205            �           2606    55402 6   auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         sushil    false    203    203    203            �           2606    55351    auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         sushil    false    203    203            �           2606    55387    auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         sushil    false    211    211            �           2606    55431 /   auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public         sushil    false    211    211    211            �           2606    55377    auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         sushil    false    209    209            �           2606    55395    auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         sushil    false    213    213            �           2606    55445 >   auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public         sushil    false    213    213    213            �           2606    55473    auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         sushil    false    209    209            �           2606    55459    django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         sushil    false    215    215            �           2606    55343 1   django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         sushil    false    201    201    201            �           2606    55341    django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         sushil    false    201    201            i           2606    55153    django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         sushil    false    182    182            �           2606    55488    django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         sushil    false    216    216            p           1259    55249 (   DDB_releases_ReleaseNumber_ef5cef76_like    INDEX     �   CREATE INDEX "DDB_releases_ReleaseNumber_ef5cef76_like" ON public."DDB_releases" USING btree ("ReleaseNumber" varchar_pattern_ops);
 >   DROP INDEX public."DDB_releases_ReleaseNumber_ef5cef76_like";
       public         sushil    false    189            �           1259    55271 $   DDB_sanity_results_Setup_id_71656cee    INDEX     m   CREATE INDEX "DDB_sanity_results_Setup_id_71656cee" ON public."DDB_sanity_results" USING btree ("Setup_id");
 :   DROP INDEX public."DDB_sanity_results_Setup_id_71656cee";
       public         sushil    false    199            �           1259    55272 )   DDB_sanity_results_Setup_id_71656cee_like    INDEX     �   CREATE INDEX "DDB_sanity_results_Setup_id_71656cee_like" ON public."DDB_sanity_results" USING btree ("Setup_id" varchar_pattern_ops);
 ?   DROP INDEX public."DDB_sanity_results_Setup_id_71656cee_like";
       public         sushil    false    199            |           1259    55262 (   DDB_setup_info_CurrentUserId_id_e6b22f76    INDEX     u   CREATE INDEX "DDB_setup_info_CurrentUserId_id_e6b22f76" ON public."DDB_setup_info" USING btree ("CurrentUserId_id");
 >   DROP INDEX public."DDB_setup_info_CurrentUserId_id_e6b22f76";
       public         sushil    false    197            }           1259    55263 -   DDB_setup_info_CurrentUserId_id_e6b22f76_like    INDEX     �   CREATE INDEX "DDB_setup_info_CurrentUserId_id_e6b22f76_like" ON public."DDB_setup_info" USING btree ("CurrentUserId_id" varchar_pattern_ops);
 C   DROP INDEX public."DDB_setup_info_CurrentUserId_id_e6b22f76_like";
       public         sushil    false    197            ~           1259    55264 "   DDB_setup_info_OwnerId_id_b6c7ee0f    INDEX     i   CREATE INDEX "DDB_setup_info_OwnerId_id_b6c7ee0f" ON public."DDB_setup_info" USING btree ("OwnerId_id");
 8   DROP INDEX public."DDB_setup_info_OwnerId_id_b6c7ee0f";
       public         sushil    false    197                       1259    55265 '   DDB_setup_info_OwnerId_id_b6c7ee0f_like    INDEX     �   CREATE INDEX "DDB_setup_info_OwnerId_id_b6c7ee0f_like" ON public."DDB_setup_info" USING btree ("OwnerId_id" varchar_pattern_ops);
 =   DROP INDEX public."DDB_setup_info_OwnerId_id_b6c7ee0f_like";
       public         sushil    false    197            �           1259    55261 &   DDB_setup_info_SetupName_ca709e0e_like    INDEX     �   CREATE INDEX "DDB_setup_info_SetupName_ca709e0e_like" ON public."DDB_setup_info" USING btree ("SetupName" varchar_pattern_ops);
 <   DROP INDEX public."DDB_setup_info_SetupName_ca709e0e_like";
       public         sushil    false    197            y           1259    55250 $   DDB_user_info_UserName_776a5d0d_like    INDEX     |   CREATE INDEX "DDB_user_info_UserName_776a5d0d_like" ON public."DDB_user_info" USING btree ("UserName" varchar_pattern_ops);
 :   DROP INDEX public."DDB_user_info_UserName_776a5d0d_like";
       public         sushil    false    196            �           1259    55480    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         sushil    false    205            �           1259    55417 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         sushil    false    207            �           1259    55418 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         sushil    false    207            �           1259    55403 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         sushil    false    203            �           1259    55433 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public         sushil    false    211            �           1259    55432 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public         sushil    false    211            �           1259    55447 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public         sushil    false    213            �           1259    55446 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public         sushil    false    213            �           1259    55474     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public         sushil    false    209            �           1259    55470 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         sushil    false    215            �           1259    55471 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         sushil    false    215            �           1259    55490 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         sushil    false    216            �           1259    55489 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         sushil    false    216            �           2606    55266 1   DDB_sanity_results_Setup_id_71656cee_fk_DDB_setup    FK CONSTRAINT     �   ALTER TABLE ONLY public."DDB_sanity_results"
    ADD CONSTRAINT "DDB_sanity_results_Setup_id_71656cee_fk_DDB_setup" FOREIGN KEY ("Setup_id") REFERENCES public."DDB_setup_info"("SetupName") DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public."DDB_sanity_results" DROP CONSTRAINT "DDB_sanity_results_Setup_id_71656cee_fk_DDB_setup";
       public       sushil    false    2178    199    197            �           2606    55251 5   DDB_setup_info_CurrentUserId_id_e6b22f76_fk_DDB_user_    FK CONSTRAINT     �   ALTER TABLE ONLY public."DDB_setup_info"
    ADD CONSTRAINT "DDB_setup_info_CurrentUserId_id_e6b22f76_fk_DDB_user_" FOREIGN KEY ("CurrentUserId_id") REFERENCES public."DDB_user_info"("UserName") DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public."DDB_setup_info" DROP CONSTRAINT "DDB_setup_info_CurrentUserId_id_e6b22f76_fk_DDB_user_";
       public       sushil    false    197    196    2171            �           2606    55256 <   DDB_setup_info_OwnerId_id_b6c7ee0f_fk_DDB_user_info_UserName    FK CONSTRAINT     �   ALTER TABLE ONLY public."DDB_setup_info"
    ADD CONSTRAINT "DDB_setup_info_OwnerId_id_b6c7ee0f_fk_DDB_user_info_UserName" FOREIGN KEY ("OwnerId_id") REFERENCES public."DDB_user_info"("UserName") DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public."DDB_setup_info" DROP CONSTRAINT "DDB_setup_info_OwnerId_id_b6c7ee0f_fk_DDB_user_info_UserName";
       public       sushil    false    2171    196    197            �           2606    55410 8   auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       sushil    false    207    2191    203            �           2606    55405 9   auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       sushil    false    2196    205    207            �           2606    55396 5   auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       sushil    false    2186    203    201            �           2606    55425 3   auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public       sushil    false    205    211    2196            �           2606    55420 1   auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public       sushil    false    2204    211    209            �           2606    55439 8   auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public       sushil    false    213    2191    203            �           2606    55434 ;   auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public       sushil    false    2204    209    213            �           2606    55460 6   django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       sushil    false    215    2186    201            �           2606    55465 1   django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public       sushil    false    2204    215    209            5	      x������ � �      7	      x������ � �      9	      x������ � �      :	      x������ � �      D	      x������ � �      B	      x������ � �      <	      x������ � �      >	      x������ � �      @	      x������ � �      A	      x������ � �      J	      x������ � �      L	      x������ � �      H	   �  x�u�ݎ�0������������HU�N�nAm:+�~Sǉ�P���|B���M���>;��
�;������σT(Xx��u%k G�O`{��&9�V��L�u�a�@��}`-@�L�cN��%�:,���j8>���x2"?;"x8"%8�Ur���q]���*�A]�܋ ���J�h��-�(���)9��g�5��������37��hW��7��1��O���`Z�Er��0Z��I�b߉A�	�N�K�u��UBh��aX��;c;g���zg��Ŗ�`C�"o�h�H.r�F���Y�ވa�#)�l�����N0�O�Qc��8�7ơ�ı�1
&��w᪊t����K�tz��n? ���D+�=��+�w)M��~;T��u%r�1tB�H'�Q"k�΁3�xj�f��7b���BE�Yz�"Dx�"��(.�$`���ر}�6?X�,t��F$�Z�O��L�\9B��E���Ԭݰ��(�ݽ���ld��wP�$%S�Uy0i�$AA)Z�yt��h�&�G�bPNU݈hh��d2��YܞL�Bx 
[�I(���,a�.�}$�[#�)@�n��H�`�{J`[�OA�w�(�7��o�q�o?m{��\(ǪnER4h;����p�\ƒ{ �a2�ׇ��?���      N	      x������ � �      P	      x������ � �      R	      x������ � �      T	      x������ � �      F	   �   x�U��� ����ٟzk|B�I,����e��;��9m���b�p���A#t�H�ڪW��%��CW��!�Ћ1x�5�V�_� ,:\��q<*�� ��1�fT�g�2��נ<@�i�YH��@6�ֽ�H�dA�����ME��8G��(Ⱦ��u~�P������.e�<��^�      3	   &  x����n�0E��Wt_D����e��(@6�Ыz�ߗrEʩX(m�s8s9$��?
 @[��T��`����7dg�3��R���8�Xd�u��� e����PRi��qzƑ[0��@f�y����.�+.".�8����ˈ�=.�M�wq�	�4�zW%1ex�]G\��##�ŅB�1:q�	W$�,�QP:8��G��k>�$���#���|;M�ޏGS�JÁ��Y�|;�tI$�FQ�M�cF�:��l��B������������������<�yk�e�������^޺���8�2�%w	�Xպ`�ۺ�gu5J�:�2W���`{?4�8.�-۸[�����(�L�IG�n��7��MPD�I"�,Z>���~ʧ��a�4�YS�qZ�
=�unLIh��2L��=WCJ�qv�/o!&%��m��Zλ�����a|̄�n��Gw��8�P�Se��:��A�qP1tƓ�����M
�Q&�ly+������DO��dB;�!-o����?�j>*AJ�ԝ*F��|�������,O��o��&      U	      x������ � �     