PGDMP     8                	    z            postgres    14.5    14.5                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    13754    postgres    DATABASE     e   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                postgres    false                       0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3334                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false                       0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    16413    address    TABLE     b   CREATE TABLE public.address (
    id_address integer NOT NULL,
    city character(80) NOT NULL
);
    DROP TABLE public.address;
       public         heap    postgres    false            �            1259    16427    ads    TABLE     �   CREATE TABLE public.ads (
    id_ads integer NOT NULL,
    name_ads character(255) NOT NULL,
    fk_author integer NOT NULL,
    price integer NOT NULL,
    description text,
    fk_adress integer NOT NULL,
    is_published boolean NOT NULL
);
    DROP TABLE public.ads;
       public         heap    postgres    false            �            1259    16483    author    TABLE     h   CREATE TABLE public.author (
    id_author integer NOT NULL,
    name_author character(255) NOT NULL
);
    DROP TABLE public.author;
       public         heap    postgres    false            �            1259    16448 
   categories    TABLE     f   CREATE TABLE public.categories (
    id_category integer NOT NULL,
    name_category character(80)
);
    DROP TABLE public.categories;
       public         heap    postgres    false            �          0    16413    address 
   TABLE DATA           3   COPY public.address (id_address, city) FROM stdin;
    public          postgres    false    210   �       �          0    16427    ads 
   TABLE DATA           g   COPY public.ads (id_ads, name_ads, fk_author, price, description, fk_adress, is_published) FROM stdin;
    public          postgres    false    211   �                  0    16483    author 
   TABLE DATA           8   COPY public.author (id_author, name_author) FROM stdin;
    public          postgres    false    213   r"       �          0    16448 
   categories 
   TABLE DATA           @   COPY public.categories (id_category, name_category) FROM stdin;
    public          postgres    false    212   �"       i           2606    16417    address adress_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.address
    ADD CONSTRAINT adress_pkey PRIMARY KEY (id_address);
 =   ALTER TABLE ONLY public.address DROP CONSTRAINT adress_pkey;
       public            postgres    false    210            k           2606    16433    ads ads_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT ads_pkey PRIMARY KEY (id_ads);
 6   ALTER TABLE ONLY public.ads DROP CONSTRAINT ads_pkey;
       public            postgres    false    211            o           2606    16487    author author_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (id_author);
 <   ALTER TABLE ONLY public.author DROP CONSTRAINT author_pkey;
       public            postgres    false    213            m           2606    16452    categories categories_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id_category);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            postgres    false    212            p           2606    16439 
   ads adress    FK CONSTRAINT     u   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT adress FOREIGN KEY (fk_adress) REFERENCES public.address(id_address);
 4   ALTER TABLE ONLY public.ads DROP CONSTRAINT adress;
       public          postgres    false    210    3177    211            q           2606    16488 
   ads author    FK CONSTRAINT     }   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT author FOREIGN KEY (fk_author) REFERENCES public.author(id_author) NOT VALID;
 4   ALTER TABLE ONLY public.ads DROP CONSTRAINT author;
       public          postgres    false    211    213    3183            �   �   x���M
�0���)r �ت��0�]((�[JWn�j���on�k��Mk`�L��7��tpG#;�`f��qA�%�FBX��fQ1��k���a���<�Dr�H~'.�!�D��[���ls#�V{����9���+�W|��(�����'z�j󀕠������z��H(^��'�o��AB3j��m����~x����H��tqj�*�>���      �   �  x��Z�n�^���jgCR���t�.�J�{�N�,���r�ԍS�u��Kj4#��f^�O�G���s��PJZ�X@69sy������n��5O��<)v�A>�'����bX��a>i�m��y\���|�n���~����|�G"�/���.��د	���PFN�P~1a���~�8[�q�Gx���0�]�8�qOe��qo0��a��ɤ6 S��W�L,͋=YX�-F~�Jnǘ���S��n�b֯�HʐE�e~*s<�wH��D��.d_aq(��}�1��¶ˏ��ő,��n/?�>�_�oa��Aq8L&��M�b�^�%F��2��uM�"O�A?�b�'�)��xr&��i�q'{�.>���Xg{����J.��;}1�"jXA$v#X�K,�/�X����H=f��؛�\�Tn.��\���F��!c��X��`�<�{�<�]��Q��X�2�I�$�`�b${2L��)����/���]�xO��/�.����y�L�]�����^��Lk]^�:��
zA���Q��?C��G*�%�g�[іD%�`\��j��I�4	�	�oin�N����F���	���u�"F�~�qﺹ����^��ޏ��L#9��8*=��TbS�}hqi{������7C����uK��.�N]�FLS9��3ƾ�Q��������Ո�>�&�y�����N��G���C����=y�[���=t�����?�Ϟ<~��g���n�y�t '_j�S���;q��x��U���A3a3��L|�T�L�+u#Mn�]z �����ϝ�2���^�i�����ۗ�A��`[�}7�yK�͙#��TP"�"�"���r���Mz[C,	�t �+��	n����Z��!蕌H��C(�@�y�}	��#�]����&3�O4 3|e3�z^���\a��ـ�*2�_��ӽ&������	�1�%��5+��-�݌a��źMUҫ�%�J���� �I&P�W�a�ZYkx�I��72vD/T��'@��Q�V	n19k�bO���ţݧ�����n*O5���Y���;�C��A~"Vz��;!�c�s+�$k��3Z}�(q�I>�+�08 �����L�^���DDLz/��.w�����j���w���؁��� ����x��T��Է`�!���1&�R�嬚�j��(eԦ��"-�86�zcD��Q�"
�V�f��
}��f�T�J�Z0�P5ycaD	�mw"_#9`1$ ��
%`\Fzo���L��m�)7[��gH��)ʑtQ^"��`V2�"�0�gL����p�����q����)߷2 R��1]�˞q$�b�L��4�āR"X�b�/�SL���w������3�SGr���P)&<d;���4��.��ܑ�D�d�Z%�+͇ܔ��.��W!��aY�̌�G��P�W+Qӟӷ�5WS��W+�V�@?���hhT��k83l�r�Z)pfůd�?�ؾ
��v���+���So��=%�<c\�V!����JЩЂ�A��(���j
�Ժ|g?$�R�7�Śio:fe1G�*g������-��,f����L�z�E�zd (��{h������[��v�*�p��޽~�.��j�؂���1&2�>�L�01ST����>��_��ݩ�8_Dij���[��2W?0�X�Efe��2/WɘNj��HX|�|<�ݔeHh�g�	>�1�؏ngPr�{ �-G�"�?��{7^�����n�V>������۳�K���,�R�
�?�K���NG�݃_]����i}�u�{IƞW@��B��xB���XjՂ6�K�!v�#�4���0������O�>�b԰譍�`#]o��X�)T#C�x-�D�#B �ʡ��dvm���]XP%k���u��n�f���VBJ�� V��[���S�KD�RZ�j��(�b�G�0O�-��T���vv��6!��\E-����DɎ[��D�-�<��֖U�mR9��3C&�Xu˼�>�Orj���J���s#{�,�b�=�yn<U�}��3�E���`�K���کU2_F��Urj5�6��p��/�ш�����=�"�ύ���"��`aA^��2)o�2"���{Y�k�]Y6�P�&԰��ڀz���A&�W���,���Y�0�M=mT���F�H�)(T�v'��6��4H�-��.(&�X�%k%��Yr|��8p��)��V�����x��������@Trqzṳ� xД���8.�l�55<x|�%!2v�m#�n7"7 t]Im����W�e�p�ׄ�)_kI��,ݔK��G)�_E#Bi��hD$�7���J]��MC�+����=.9��6��X�?�#5��l��ì����=?�ƿ9mg&3'������=]�s��~�K;�pz݂��_A?�w�Fã!q���R)2�5��;�C�I]������&t��F��J�+"���#v���Z#1���6JO0ݻ/aX����@BU�soZ�]��R��F\����OD.�3[�r3�M�̙��_B��hM,C�-�2�|n��5L��1�%bWq��D���L1T�v��Ӟ�T����ڌ�x,�(��D-���Ϋ3US�� *�H��=�����:u��Dŝ����Ƽ��h����c�W�HB��x}���K�S�B�J�Xw�)e��v��k�h(`�"a�B��1�.�mk�#��6T;���V�2��׮,N5�Q{P
$S0�L��G�W�Bk(Q��NJ���#}�W��I[�.V$?ʃZvɻi�X��=�)���~��R��<x�-wS����{5��)f aY���?Ҹ�����No);��I��7r�"=k\ڒ� 2ꂬ�yTR2���*97��dM�+��I������`p��߰<1t�`�n����U)�gGRC��;��-����j��\L�`��I獕�����eš�T�?G�W_Z4��|�^(*hK�G0�w�h�/c(q����Kñ�(���h�u�D��^��\Q�`�gQ#*����&o\���y�� '���̮'J\�%�i��6c!]�:q)�ɉ#��V�W"�YDc��d��'�٥W?[њ��X�g��#WL��E"�^��Tq�c/��4Jf�Nl�?��_�uj��F#��2l���{����?�W>���N㰽�+f��!3.sQ`�F>�/��|�rUG%�6�w��yU.%�m��H�'SK�U����A{cc�?(,5�          u   x���	�@�w�HB���c�@�i�G�\�������`�*�d*��f�I�6�^�H�!�k��w�	�sS�J :�+$>�h�8t�Md{F�ġw�����>�wxt�z ���      �   h   x�3�0�¾�Mv\�ua�� ����^l���� �����*p�p^Xpa��F`Xl���jF�r^�4t#�أ t7��{A]l��")�!F��� ��i�     