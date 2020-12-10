-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 08-Dez-2020 às 01:23
-- Versão do servidor: 10.4.14-MariaDB
-- versão do PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `formulario`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `avaliacao`
--

CREATE TABLE `avaliacao` (
  `id` int(11) NOT NULL,
  `materia_curso` varchar(255) NOT NULL,
  `prof_curso` varchar(255) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fim` time NOT NULL,
  `ultima_aula` date NOT NULL,
  `num_alunos_turma` int(11) DEFAULT NULL,
  `nota_disciplina` varchar(255) DEFAULT NULL,
  `provas_feitas` varchar(255) DEFAULT NULL,
  `descreva_experiencia` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `avaliacao`
--

INSERT INTO `avaliacao` (`id`, `materia_curso`, `prof_curso`, `hora_inicio`, `hora_fim`, `ultima_aula`, `num_alunos_turma`, `nota_disciplina`, `provas_feitas`, `descreva_experiencia`) VALUES
(17, '', '', '00:00:00', '00:00:00', '0000-00-00', 0, '', ',,', ''),
(18, '', '', '00:00:00', '00:00:00', '0000-00-00', 0, '', ',,', ''),
(19, '', '', '00:00:00', '00:00:00', '0000-00-00', 0, '', ',,', ''),
(20, 'Banco de Dados', 'Bruno Zonovelli da Silva', '00:54:00', '00:54:00', '2020-12-10', 6, '5', 'AV1,AV2,AV3', '32131231231231231'),
(21, 'Banco de Dados', 'Ronney Moreira de Castro', '06:55:00', '06:55:00', '2020-12-30', 10, '5', 'AV1,AV2,AV3', 'dasdasddaasdasda'),
(22, 'Computação em Nuvem', 'Jose Luiz Andrade Kessler', '03:56:00', '03:56:00', '2020-12-13', 12, '5', 'AV1,AV2,AV3', '2321312312312312'),
(23, 'Banco de Dados', 'Bruno Zonovelli da Silva', '02:58:00', '02:58:00', '2020-12-16', 3, '5', 'AV1,AV2,AV3', '21321321312312'),
(24, 'Desenvolvimento Web', 'Bruno Zonovelli da Silva', '04:00:00', '04:00:00', '2020-12-08', 10, '5', ',AV2,AV3', '31231312312'),
(25, '', '', '00:00:00', '00:00:00', '0000-00-00', 0, '', ',,', ''),
(26, '', '', '00:00:00', '00:00:00', '0000-00-00', 0, '', ',,', ''),
(27, 'Banco de Dados', 'Ronney Moreira de Castro', '02:27:00', '02:27:00', '2020-12-16', 10, '', 'AV1,AV2,AV3', '321312312321'),
(28, 'Banco de Dados', 'Ronney Moreira de Castro', '04:28:00', '04:28:00', '2020-12-17', 13, '5', 'AV1,AV2,', '321312312312321'),
(29, 'Banco de Dados', 'Ronney Moreira de Castro', '05:29:00', '07:29:00', '2020-12-22', 0, '5', 'AV1,AV2,AV3', '3321312312312'),
(30, 'Banco de Dados', 'Ronney Moreira de Castro', '18:50:00', '21:40:00', '2020-11-30', 50, '5', 'AV1,AV2,', 'Nice!!!'),
(31, 'Banco de Dados', 'Ronney Moreira de Castro', '03:20:00', '03:23:00', '2020-12-23', 5, '5', 'AV1,AV2,AV3', '553454353453'),
(34, 'Desenvolvimento Web', 'Bruno Zonovelli da Silva', '07:47:00', '09:47:00', '2020-12-16', 53, '5', 'AV1,AV2,', 'Project Final'),
(35, 'Computação em Nuvem', 'Jose Luiz Andrade Kessler', '09:50:00', '12:50:00', '2020-12-15', 55, '5', 'AV1,AV2,AV3', 'test 123'),
(36, 'Python', 'Ronney Moreira de Castro', '04:51:00', '07:51:00', '2020-12-23', 63, '5', 'AV1,,', 'test python'),
(37, 'Python', 'Ronney Moreira de Castro', '03:58:00', '03:57:00', '2020-12-28', 9, '5', 'AV1,AV2,', 'test Python'),
(38, 'Banco de Dados', 'Ronney Moreira de Castro', '15:00:00', '19:59:00', '2020-12-21', 6, '5', 'AV1,AV2,AV3', '543545345345435'),
(39, 'Python', 'Ronney Moreira de Castro', '16:07:00', '19:07:00', '2020-12-21', 9, '5', 'AV1,AV2,AV3', '42342');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `avaliacao`
--
ALTER TABLE `avaliacao`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avaliacao`
--
ALTER TABLE `avaliacao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
