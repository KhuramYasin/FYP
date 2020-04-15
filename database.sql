USE [master]
GO

/****** Object:  Database [FYP]    Script Date: 15/04/2020 6:05:28 PM ******/
CREATE DATABASE [FYP]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'FYP', FILENAME = N'D:\Study\FYP\FYP_1 test\FYP.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'FYP_log', FILENAME = N'D:\Study\FYP\FYP_1 test\DBLOG(DOn''t change anything)\FYP_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [FYP].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [FYP] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [FYP] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [FYP] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [FYP] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [FYP] SET ARITHABORT OFF 
GO

ALTER DATABASE [FYP] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [FYP] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [FYP] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [FYP] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [FYP] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [FYP] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [FYP] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [FYP] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [FYP] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [FYP] SET  DISABLE_BROKER 
GO

ALTER DATABASE [FYP] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [FYP] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [FYP] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [FYP] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [FYP] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [FYP] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [FYP] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [FYP] SET RECOVERY SIMPLE 
GO

ALTER DATABASE [FYP] SET  MULTI_USER 
GO

ALTER DATABASE [FYP] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [FYP] SET DB_CHAINING OFF 
GO

ALTER DATABASE [FYP] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [FYP] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [FYP] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [FYP] SET QUERY_STORE = OFF
GO

ALTER DATABASE [FYP] SET  READ_WRITE 
GO
